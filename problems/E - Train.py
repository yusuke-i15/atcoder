from collections import defaultdict
import heapq
N,M,X,Y = map(int,input().split())
G = defaultdict(list)
for i in range(M):
    u,v,t,k = map(int,input().split())
    G[u].append((v,t,k))
    G[v].append((u,t,k))
#dist:開始点からの距離_今回はノード0
dist = defaultdict(lambda: float("inf"))
seen = [False]*(N+1)
dist[X] = 0
q = [(0,X)]
heapq.heapify(q)
while(len(q) > 0):
    v = heapq.heappop(q)[1]
    if seen[v] == True:
        continue
    seen[v] = True
    for next_v,nt,nk in G[v]:
        if not seen[next_v] and dist[next_v] > dist[v] + (nk-dist[v]%nk)%nk + nt:
            dist[next_v] = dist[v] + (nk-dist[v]%nk)%nk + nt
            heapq.heappush(q,(dist[next_v],next_v))
if dist[Y] == float("inf"):
    print(-1)
else:
    print(dist[Y])