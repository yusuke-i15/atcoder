mod = 10 ** 9 + 7
def comb(k):
    ret = 1
    for i in range(k):
        ret *= (n - i) * pow(i + 1, mod - 2, mod)
        ret %= mod
    return ret

n,a,b = map(int,input().split())
ans = pow(2,n,mod)-1
ans -= comb(a)
ans -= comb(b)
ans = ans%mod
print(ans)
