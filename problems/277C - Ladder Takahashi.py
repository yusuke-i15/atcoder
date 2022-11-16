from collections import deque
from collections import defaultdict
G = defaultdict(list)
N = int(input())
for i in range(N):
    A,B = map(int,input().split())
    G[A].append(B)
    G[B].append(A)
ans = 1

#dist:開始点からの距離_今回はノード0
dist = defaultdict(lambda: -1)
dist[1] = 1
q = deque()
q.append(1)

while(len(q) > 0):
    v = q.popleft()
    for next_v in G[v]:
        if dist[next_v] == -1:
            q.append(next_v)
            dist[next_v] = dist[v] + 1
            ans = max(ans,next_v)
print(ans)