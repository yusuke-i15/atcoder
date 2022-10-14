W,H = map(int,input().split())

def nCr(n,r):
    fac = [1]*(n+1)
    mod = 10**9+7
    for i in range(n):
        fac[i+1] = fac[i]*(i+1)%mod
    ans = fac[n]*pow(fac[r],mod-2,mod)*pow(fac[n-r],mod-2,mod)%mod
    return ans