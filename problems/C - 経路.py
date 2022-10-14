W,H = map(int,input().split())
fac = [1]*(2*10**5)
mod = 10**9+7
for i in range(W+H-2):
    fac[i+1] = fac[i]*(i+1)%mod

ans = fac[W+H-2]*pow(fac[H-1],mod-2,mod)*pow(fac[W-1],mod-2,mod)%mod
print(ans)