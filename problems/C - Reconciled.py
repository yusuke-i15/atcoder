N,M = map(int,input().split())
mod = 10**9 + 7
def facto(n):
    tmp = 1
    for i in range(2,n+1):
        tmp *= i
        tmp %= mod
    return tmp
if abs(N-M) == 1:
    print(facto(N)*facto(M)%mod)
elif N == M:
    print(facto(N)*facto(M)*2%mod)
else:
    print(0)