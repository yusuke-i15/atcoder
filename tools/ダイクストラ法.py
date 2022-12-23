"""
負の辺を含まない重み付きグラフの単一視点最短経路問題
O(ElogV)
"""
from collections import defaultdict
import heapq

G = defaultdict(list)

V,E,r = map(int,input().split())

for i in range(E):
    s,t,d = map(int,input().split())
    G[s].append((t,d))

seen = [False] * V
dist = [10**10] * V
dist[r] = 0
q = [(0,r)]
heapq.heapify(q)
while(len(q)>0):
    v = heapq.heappop(q)[1]
    seen[v] = True
    for next in G[v]:
        if not seen[next[0]] and dist[next[0]] > dist[v] + next[1]:
            dist[next[0]] = dist[v] + next[1]
            heapq.heappush(q,(dist[next[0]],next[0]))
for i in range(V):
    print(dist[i] if dist[i] != 10**10 else "INF")