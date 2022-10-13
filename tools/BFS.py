from collections import deque
from collections import defaultdict
G = defaultdict(list)
E = [(0,1),(0,2),(1,2),(1,3),(2,3)]
for i in E:
    u = i[0]
    v = i[1]
    G[u].append(v)
    G[v].append(u)
print(G)

#dist:開始点からの距離_今回はノード0
dist = defaultdict(lambda: -1)
dist[0] = 0
q = deque()
q.append(0)

while(len(q) > 0):
    v = q.popleft()
    for next_v in G[v]:
        if dist[next_v] == -1:
            q.append(next_v)
            dist[next_v] = dist[v] + 1
print(dist)

G[0].remove(1)
print(G)