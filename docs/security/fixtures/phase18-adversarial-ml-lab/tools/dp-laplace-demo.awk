function laplace(epsilon,    r,u,a,sgn) {

    r=rand()

    # Guard the inverse-CDF calculation against exact endpoints.
    if (r <= 0) {
        r=0.000000000001
    }

    if (r >= 1) {
        r=0.999999999999
    }

    u=r-0.5
    a=(u<0 ? -u : u)
    sgn=(u<0 ? -1 : 1)

    return -(1/epsilon)*sgn*log(1-(2*a))
}

BEGIN {

    OFS=","

    srand()

    epsilon[1]=0.5
    epsilon[2]=1
    epsilon[3]=2

    print \
      "dataset", \
      "epsilon", \
      "scale", \
      "sample", \
      "true_count", \
      "noise", \
      "noisy_count"

    for (e=1; e<=3; e++) {

        eps=epsilon[e]
        scale=1/eps

        for (dataset=1; dataset<=2; dataset++) {

            if (dataset==1) {
                count=count_a
                name="D"
            } else {
                count=count_b
                name="D_neighbor"
            }

            for (i=1; i<=samples; i++) {

                noise=laplace(eps)
                noisy=count+noise

                print \
                  name, \
                  eps, \
                  scale, \
                  i, \
                  count, \
                  noise, \
                  noisy
            }
        }
    }
}
