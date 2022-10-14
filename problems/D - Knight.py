X, Y = map(int,input().split())

twoY_X = 2*Y-X
twoX_Y = 2*X-Y
if twoY_X%3 != 0 or twoX_Y%3 != 0:
    print(0)
else:
    a = twoY_X//3
    b = twoX_Y//3
    if a < 0 or b <0:
        print(0)
    else:
        fac = [1]*(2*10**6)
        mod = 10**9+7
        for i in range(a+b):
            fac[i+1] = fac[i]*(i+1)%mod

        ans = fac[a+b]*pow(fac[a],mod-2,mod)*pow(fac[b],mod-2,mod)%mod
        print(ans)