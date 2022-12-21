from collections import deque
from collections import defaultdict

a,N = map(int,input().split())

#dist:開始点からの距離_今回はノード0
dist = defaultdict(lambda: -1)
seen = defaultdict(int)
dist[1] = 0
q = deque()
q.append(1)

while(len(q) > 0):
    v = q.popleft()
    if seen[v] != 0:
        continue
    if v == N:
        break
    if v >= 10 and v%10 != 0:
        tmp = str(v)
        next_v = int(tmp[-1] + tmp[:-1])

        dist[next_v] = dist[v] + 1
        q.append(next_v)
    next_v = v*a
    if next_v < 10**6:
        q.append(next_v)
        dist[next_v] = dist[v] + 1
    seen[v] += 1        
print(dist[N])
