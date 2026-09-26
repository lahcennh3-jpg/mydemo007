#!/usr/bin/env bash
set -euo pipefail

SOURCE_COMMIT=193c7c4b652fc3ae76256718f53d0a956e996b7f
BASE_IMAGE_ID=sha256:fa570e141e39af5e1e48767fe14cbe227abe9a5ec0e3d08b9580c8bf60b35543
API_CONTAINER=onyx-api_server-1
BASE_TAG=localhost/phase25-cached-backend:fa570e141e39
OUTPUT_TAG=localhost/phase25-six-file-overlay:193c7c4b652f

source_files=(
  backend/onyx/server/features/mcp/models.py
  backend/onyx/utils/redaction.py
  backend/onyx/tools/tool_runner.py
  backend/onyx/tools/models.py
  backend/onyx/background/celery/tasks/user_file_processing/tasks.py
  backend/onyx/configs/constants.py
)

cd "$(git rev-parse --show-toplevel)"
case "$(git remote get-url origin)" in
  https://github.com/lahcennh3-jpg/mydemo007|https://github.com/lahcennh3-jpg/mydemo007.git) ;;
  *) echo 'STOP: repository origin differs from the approved fork' >&2; exit 1 ;;
esac
if ! git merge-base --is-ancestor "$SOURCE_COMMIT" HEAD ||
   [ -n "$(git status --porcelain)" ]
then
  echo 'STOP: source ancestry or clean worktree check failed' >&2
  exit 1
fi

api_before="$(docker inspect -f '{{.Id}} {{.Image}}' "$API_CONTAINER")"
if [ "$(docker inspect -f '{{.Image}}' "$API_CONTAINER")" != "$BASE_IMAGE_ID" ]; then
  echo 'STOP: running API image changed' >&2
  exit 1
fi

driver="$(docker buildx inspect | awk '$1 == "Driver:" {print $2; exit}')"
if [ "$driver" != docker ]; then
  echo 'STOP: the selected builder cannot use the local Docker image store' >&2
  exit 1
fi

onbuild="$(docker image inspect -f '{{json .Config.OnBuild}}' "$BASE_IMAGE_ID")"
case "$onbuild" in
  null|'[]') ;;
  *) echo 'STOP: base image has ONBUILD steps' >&2; exit 1 ;;
esac

available_mib="$(awk '/MemAvailable:/ {print int($2 / 1024)}' /proc/meminfo)"
available_kib="$(df -Pk /workspaces | awk 'NR == 2 {print $4}')"
if [ "$available_mib" -lt 1536 ] ||
   [ "$available_kib" -lt 8388608 ]
then
  echo 'STOP: less than 1.5 GiB memory or 8 GiB disk is available' >&2
  exit 1
fi

for file in "${source_files[@]}"; do
  mode="$(git ls-tree "$SOURCE_COMMIT" -- "$file" | awk '{print $1}')"
  size="$(git cat-file -s "$SOURCE_COMMIT:$file")"
  if [ "$mode" != 100644 ] || [ "$size" -gt 1048576 ]; then
    echo "STOP: source file mode or size changed: $file" >&2
    exit 1
  fi
done

if docker image inspect "$BASE_TAG" >/dev/null 2>&1; then
  if [ "$(docker image inspect -f '{{.Id}}' "$BASE_TAG")" != "$BASE_IMAGE_ID" ]; then
    echo 'STOP: local base tag points to another image' >&2
    exit 1
  fi
else
  docker tag "$BASE_IMAGE_ID" "$BASE_TAG"
fi

if docker image inspect "$OUTPUT_TAG" >/dev/null 2>&1; then
  echo 'STOP: output tag exists; preserve it for review' >&2
  exit 1
fi

context="$(mktemp -d /tmp/phase25-overlay-context.XXXXXX)"
evidence="$(mktemp -d /tmp/phase25-overlay-evidence.XXXXXX)"
git archive --format=tar "$SOURCE_COMMIT" -- "${source_files[@]}" |
  tar -xf - -C "$context"

cat > "$context/Dockerfile" <<DOCKERFILE
FROM $BASE_TAG
LABEL ai.security.source_overlay_commit="$SOURCE_COMMIT"
LABEL ai.security.base_image_id="$BASE_IMAGE_ID"
LABEL ai.security.overlay_scope="six_selected_python_files"
COPY --chown=1001:1001 backend/onyx/server/features/mcp/models.py /app/onyx/server/features/mcp/models.py
COPY --chown=1001:1001 backend/onyx/utils/redaction.py /app/onyx/utils/redaction.py
COPY --chown=1001:1001 backend/onyx/tools/tool_runner.py /app/onyx/tools/tool_runner.py
COPY --chown=1001:1001 backend/onyx/tools/models.py /app/onyx/tools/models.py
COPY --chown=1001:1001 backend/onyx/background/celery/tasks/user_file_processing/tasks.py /app/onyx/background/celery/tasks/user_file_processing/tasks.py
COPY --chown=1001:1001 backend/onyx/configs/constants.py /app/onyx/configs/constants.py
DOCKERFILE

echo "BUILD_CONTEXT=$context"
echo "EVIDENCE_DIR=$evidence"
timeout --signal=TERM --kill-after=5s 60s \
  docker build --network none --pull=false --progress=plain \
  --tag "$OUTPUT_TAG" "$context" > "$evidence/build.log" 2>&1 ||
  { tail -40 "$evidence/build.log" >&2; echo 'BUILD=FAILED' >&2; exit 1; }

image_paths=()
for file in "${source_files[@]}"; do
  image_paths+=("/app/${file#backend/}")
done

manifest="$(timeout 10s docker run --rm --pull=never --network none \
  --read-only --pids-limit 64 --memory 512m --cpus 1 \
  -e PYTHONDONTWRITEBYTECODE=1 --entrypoint python "$OUTPUT_TAG" \
  -c 'import hashlib,sys; [print(hashlib.sha256(open(p,"rb").read()).hexdigest()) for p in sys.argv[1:]]' \
  "${image_paths[@]}")"
mapfile -t image_hashes <<< "$manifest"
if [ "${#image_hashes[@]}" -ne "${#source_files[@]}" ]; then
  echo 'STOP: image hash count differs from source file count' >&2
  exit 1
fi

{
  printf 'source_commit\t%s\n' "$SOURCE_COMMIT"
  printf 'base_image_id\t%s\n' "$BASE_IMAGE_ID"
  printf 'overlay_tag\t%s\n' "$OUTPUT_TAG"
  printf 'overlay_image_id\t%s\n' "$(docker image inspect -f '{{.Id}}' "$OUTPUT_TAG")"
  printf 'dockerfile_sha256\t%s\n' "$(sha256sum "$context/Dockerfile" | awk '{print $1}')"

  for i in "${!source_files[@]}"; do
    file="${source_files[$i]}"
    source_hash="$(git show "$SOURCE_COMMIT:$file" | sha256sum | awk '{print $1}')"
    image_hash="${image_hashes[$i]}"
    if [ "$source_hash" != "$image_hash" ]; then
      echo "STOP: image file differs from pinned source: $file" >&2
      exit 1
    fi
    printf 'MATCH\t%s\t%s\n' "$file" "$source_hash"
  done
} | tee "$evidence/manifest.tsv"

if [ "$(docker inspect -f '{{.Id}} {{.Image}}' "$API_CONTAINER")" != "$api_before" ]; then
  echo 'STOP: running API identity changed during preparation' >&2
  exit 1
fi

echo 'IMAGE_ONLY_PREPARATION=PASS'
echo 'RUNNING_API_AND_DATABASE=UNTOUCHED_BY_THIS_SCRIPT'
echo 'FULL_SOURCE_BUILD_AND_RUNTIME_CORRESPONDENCE=NOT_ESTABLISHED'
