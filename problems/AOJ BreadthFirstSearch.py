from collections import deque
from collections import defaultdict
G = defaultdict(list)

n = int(input())
for i in range(n):
    ukv = list(map(int,input().split()))
    for i in range(ukv[1]):
        G[ukv[0]].append(ukv[i+2])

dist = defaultdict(lambda: -1)
dist[1] = 0
q = deque()
q.append(1)

while(len(q) > 0):
    v = q.popleft()
    for next_v in G[v]:
        if dist[next_v] == -1:
            q.append(next_v)
            dist[next_v] = dist[v] + 1
for i in range(1,n+1):
    print(i,dist[i])