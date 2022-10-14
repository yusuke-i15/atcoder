N,Q = map(int,input().split())
a = list(map(int,input().split()))
c = [1] + list(map(int,input().split())) + [1]

ans = 0
mod = 1000000007
S = [0]*(N)
for i in range(N-1):
    S[i+1] = S[i] + pow(a[i],a[i+1],mod)
for i in range(Q+1):
    ans += abs(S[c[i+1]-1]-S[c[i]-1])
    ans %= mod
print(ans)    