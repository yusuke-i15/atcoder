from collections import defaultdict
from collections import deque

R,C = map(int,input().split())
sx,sy = map(int,input().split())
gx,gy = map(int,input().split())
c = [list(input()) for i in range(R)]
sx -= 1
sy -= 1
gx -= 1
gy -= 1

dist = defaultdict(lambda: defaultdict(lambda: -1))
q = deque()
q.append((sx,sy))
dist[sx][sy] = 0
tate = [1,0,-1,0]
yoko = [0,1,0,-1]
while(len(q)>0):
    v = q.popleft()
    for i in range(4):
        next_x = v[0] + yoko[i]
        next_y = v[1] + tate[i]
        if dist[next_x][next_y] == -1 and c[next_x][next_y] == ".":
            q.append((next_x,next_y))
            dist[next_x][next_y] = dist[v[0]][v[1]] + 1
print(dist[gx][gy])