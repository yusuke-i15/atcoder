from collections import defaultdict
from collections import deque

H,W,N = map(int,input().split())
c = [list(input()) for i in range(H)]

for i in range(H):
    for j in range(W):
        if c[i][j] == "S":
            sx = i
            sy = j


tate = [1,0,-1,0]
yoko = [0,1,0,-1]

ans = 0
for cheeze in range(1,N+1):
    dist = defaultdict(lambda: defaultdict(lambda: -1))
    q = deque()
    q.append((sx,sy))
    dist[sx][sy] = 0
    while(len(q)>0):
        v = q.popleft()
        for i in range(4):
            next_x = v[0] + yoko[i]
            next_y = v[1] + tate[i]
            if next_x >= 0 and next_x < H and next_y >= 0 and next_y < W:
                if dist[next_x][next_y] == -1 and c[next_x][next_y] != "X":
                    q.append((next_x,next_y))
                    dist[next_x][next_y] = dist[v[0]][v[1]] + 1
                    if c[next_x][next_y] == str(cheeze):
                        ans += dist[next_x][next_y]
                        sx = next_x
                        sy = next_y
                        q = deque()
                    
print(ans)