from collections import deque
from collections import defaultdict
N,M = map(int,input().split())
G = defaultdict(list)
for i in range(M):
    u,v = map(int,input().split())
    G[u].append(v)
    G[v].append(u)

#dist:開始点からの距離_今回はノード0
dist = defaultdict(lambda: -1)
dist[1] = 0
q = deque()
q.append(1)

while(len(q) > 0):
    v = q.popleft()
    for next_v in G[v]:
        if dist[next_v] == -1:
            q.append(next_v)
            dist[next_v] = v
print("Yes")
for i in range(2,N+1):
    print(dist[i])
