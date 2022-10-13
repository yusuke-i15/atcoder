N,M = map(int,input().split())
P = list(map(int,input().split()))

S = [0]*(N+1)
for i in range(M-1):
    S[min(P[i],P[i+1])-1] += 1
    S[max(P[i],P[i+1])-1] -= 1
for i in range(N):
    S[i+1] += S[i]
ans = 0

for i in range(N-1):
    a,b,c = map(int,input().split())
    count = S[i]
    ans += min(count*a,count*b+c)

print(ans)