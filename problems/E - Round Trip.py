from collections import defaultdict
from collections import deque

H,W = map(int,input().split())
C = [input() for i in range(H)]
s = []
tate = [1,0,-1,0]
yoko = [0,1,0,-1]
for i in range(H):
    for j in range(W):
        if C[i][j] == "S":
            for k in range(4):
                next_x = i + yoko[k]
                next_y = j + tate[k]
                #番兵法ないとき
                if next_x < 0 or next_x >= H or next_y < 0 or next_y >= W:
                    continue
                if C[next_x][next_y] == ".":
                    s.append((next_x,next_y))
flag = False
for sx,sy in s:
    dist = defaultdict(lambda: defaultdict(lambda: -1))
    q = deque()
    q.append((sx,sy))
    dist[sx][sy] = 0
    while(len(q)>0):
        v = q.popleft()
        for i in range(4):
            next_x = v[0] + yoko[i]
            next_y = v[1] + tate[i]
            #番兵法ないとき
            if next_x < 0 or next_x >= H or next_y < 0 or next_y >= W:
                continue
            if dist[next_x][next_y] == -1 and C[next_x][next_y] == ".":
                q.append((next_x,next_y))
                dist[next_x][next_y] = dist[v[0]][v[1]] + 1
    for gx,gy in s:
        if dist[gx][gy] > 0:
            flag = True
print("Yes" if flag else "No")
