N,K = map(int,input().split())
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
for i in range(1,K+1):
    print(nCk(N-K+1,i)*nCk(K-1,i-1)%mod)