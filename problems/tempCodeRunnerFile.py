    n = temp//3*2 + dif
    r = temp//3 + dif

    fac = [1]*(2*10**6)
    mod = 10**9+7
    for i in range(n):
        fac[i+1] = fac[i]*(i+1)%mod

    ans = fac[n]*pow(fac[r],mod-2,mod)*pow(fac[n-r],mod-2,mod)%mod
    print(ans)