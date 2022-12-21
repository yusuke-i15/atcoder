mod = 10**9 + 7
def nCk(n, k):
    under = 1
    for x in range(1, k+1):
        under *= x
        under %= mod
    over = 1
    for x in range(n, n-k, -1):
        over *= x
        over %= mod
    under = pow(under, mod-2, mod)
    return (under%mod)*(over%mod)

S = int(input())
tmp = 1
ans = 0
while(tmp*3<=S):
    ans += nCk(S-tmp*3+tmp-1,tmp-1)
    ans %= mod
    tmp += 1
print(ans)