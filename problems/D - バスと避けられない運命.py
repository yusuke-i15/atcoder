N,M = map(int,input().split())

inf = float("inf")
dist = [[inf]*N for i in range(N)]
for i in range(N):
    dist[i][i] = 0
for i in range(M):
    a,b,t = map(int,input().split())
    if t < dist[a-1][b-1]:
        dist[a-1][b-1] = t
        dist[b-1][a-1] = t

for k in range(N):
    for i in range(N):
        for j in range(N):
            dist[i][j] = min(dist[i][j],dist[i][k]+dist[k][j])
ans = inf 
for i in range(N):
    ans = min(ans,max(dist[i]))
print(ans)