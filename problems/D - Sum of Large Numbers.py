mod = 10**9 + 7
N,K = map(int,input().split())
ans = 0
mi = sum(range(K))
ma = sum(range(N,N-K,-1))
for i in range(K,N+2):
    ans += (ma-mi+1)
    mi += i
    ma += N - i
    ans %= mod
print(ans)