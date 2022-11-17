W,H = map(int,input().split())
import math
def comb(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
base = comb(5,3)

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

mod = 10 ** 9 + 7
def comb(k):
    ret = 1
    for i in range(k):
        ret *= (n - i) * pow(i + 1, mod - 2, mod)
        ret %= mod
    return ret