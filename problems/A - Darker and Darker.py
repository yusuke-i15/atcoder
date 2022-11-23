from collections import defaultdict
from collections import deque

H,W = map(int,input().split())
A = [input() for i in range(H)]
q = deque()
dist = defaultdict(lambda: defaultdict(lambda: -1))
for i in range(H):
    for j in range(W):
        if A[i][j] == "#":
            q.append((i,j))
            dist[i][j] = 0
tate = [1,0,-1,0]
yoko = [0,1,0,-1]
ans = 0
while(len(q)>0):
    v = q.popleft()
    for i in range(4):
        next_x = v[0] + yoko[i]
        next_y = v[1] + tate[i]
        if next_x < 0 or next_x >= H or next_y < 0 or next_y >= W:
            continue
        if dist[next_x][next_y] == -1:
            q.append((next_x,next_y))
            dist[next_x][next_y] = dist[v[0]][v[1]] + 1
            ans = max(ans,dist[next_x][next_y])
print(ans)
    