from collections import defaultdict
from collections import deque

W, H = map(int,input().split())
c = [[0]*(W+2) for i in range(H+2)]
for i in range(1,H+1):
    c[i][1:W+1] = list(map(int,input().split()))
yoko_e = [-1,-1,-1,0,1,0]
tate_e = [1,0,-1,-1,0,1]
yoko_o = [-1,0,1,1,1,0]
tate_o = [0,-1,-1,0,1,1]

dist = defaultdict(lambda: defaultdict(lambda: -1))

def bfs(sx,sy):
    q = deque()
    q.append((sx,sy))
    dist[sx][sy] = 0
    count = 0
    while(len(q)>0):
        v = q.popleft()
        for i in range(6):
            if v[0]%2 == 0:
                next_x = v[0] + tate_e[i]
                next_y = v[1] + yoko_e[i]
            elif v[0]%2 == 1:
                next_x = v[0] + tate_o[i]
                next_y = v[1] + yoko_o[i]
            if next_x < 0 or next_x >= H+2 or next_y < 0 or next_y >= W+2:
                continue
            if c[next_x][next_y] == 1:
                count += 1
            if dist[next_x][next_y] == -1 and c[next_x][next_y] == 0:
                q.append((next_x,next_y))
                dist[next_x][next_y] = dist[v[0]][v[1]] + 1         
    return count
ans = bfs(0,0)
print(ans)
