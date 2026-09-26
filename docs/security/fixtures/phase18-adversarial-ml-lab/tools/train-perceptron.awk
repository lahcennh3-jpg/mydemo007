BEGIN {
    FS=","

    w1=0
    w2=0
    w3=0
    b=0

    epochs=30
}

NR==1 {
    next
}

{
    n++

    x1[n]=$2+0
    x2[n]=$3+0
    x3[n]=$4+0
    y[n]=$5+0
}

END {
    for (e=1; e<=epochs; e++) {
        for (i=1; i<=n; i++) {

            score=(w1*x1[i])+(w2*x2[i])+(w3*x3[i])+b
            pred=(score >= 0 ? 1 : 0)
            err=y[i]-pred

            w1 += err*x1[i]
            w2 += err*x2[i]
            w3 += err*x3[i]
            b  += err
        }
    }

    printf "w1=%g\nw2=%g\nw3=%g\nbias=%g\nepochs=%d\n", \
        w1,w2,w3,b,epochs
}
