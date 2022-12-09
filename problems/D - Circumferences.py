from collections import defaultdict
from collections import deque
N = int(input())
sx,sy,tx,ty = map(int,input().split())
xyr = [tuple(map(int,input().split())) for i in range(N)]
start = []
goal = []
for i in range(N):
    x,y,r = xyr[i]
    if (sx-x)**2 + (sy-y)**2 == r**2:
        start.append(i)
    if (tx-x)**2 + (ty-y)**2 == r**2:
        goal.append(i)
G = defaultdict(list)
for i in range(N):
    x1,y1,r1 = xyr[i]
    for j in range(i,N):
        if i == j:
            continue
        x2,y2,r2 = xyr[j]
        d = (x1-x2)**2 + (y1-y2)**2
        if (r1-r2)**2 <=d and d<=(r1+r2)**2:
            G[i].append(j)
            G[j].append(i)
#dist:開始点からの距離_今回はノード0
dist = defaultdict(lambda: -1)
flag = False
for i in start:
    if dist[i] == -1:
        dist[i] = 0
        q = deque()
        q.append(i)
        while(len(q) > 0):
            v = q.popleft()
            for next_v in G[v]:
                if dist[next_v] == -1:
                    q.append(next_v)
                    dist[next_v] = dist[v] + 1
    for j in goal:
        if dist[j] != -1:
            flag = True
            break
    if flag:
        break
print('Yes' if flag else 'No')