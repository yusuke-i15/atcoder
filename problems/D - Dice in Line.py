N,K = map(int,input().split())
p = list(map(int,input().split()))
rui = [0]*(N+1)
for i in range(N):
    rui[i+1] = rui[i] + p[i]
ans = 0
for i in range(N-K+1):
    temp = rui[i+K] - rui[i]
    ans = max(ans,temp*0.5)
print(ans+0.5*K)