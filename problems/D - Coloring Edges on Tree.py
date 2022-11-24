from collections import defaultdict
from collections import deque
N = int(input())
G = defaultdict(list)
ans = []
for i in range(N-1):
    a,b = map(int,input().split())
    G[a].append(b)
    G[b].append(a)
    if a < b:
        ans.append((a,b))
    else:
        ans.append((b,a))
K = 0
argK = 0
for i in range(1,N+1):
    if len(G[i]) > K:
        K = len(G[i])
        argK = i
use_c = defaultdict(list)
print(K)
dist = defaultdict(lambda: -1)
ansC = defaultdict(int)
dist[argK] = 0
q = deque()
q.append(argK)

while(len(q) > 0):
    v = q.popleft()
    col = 1
    for next_v in G[v]:
        if dist[next_v] == -1:
            q.append(next_v)
            dist[next_v] =  1
            if col == use_c[v]:
                col += 1
            if v < next_v:
                ansC[(v,next_v)] = col
            else:
                ansC[(next_v,v)] = col
            use_c[next_v] = col
            col += 1
for i in range(N-1):
    print(ansC[ans[i]])