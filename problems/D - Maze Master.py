from collections import defaultdict
from collections import deque
H,W = map(int,input().split())
S = [input() for i in range(H)]
ans = 0
for sx in range(H):
    for sy in range(W):
        if S[sx][sy] == "#":
            continue
        dist = defaultdict(lambda: defaultdict(lambda: -1))
        q = deque()
        q.append((sx,sy))
        dist[sx][sy] = 0
        tate = [1,0,-1,0]
        yoko = [0,1,0,-1]
        tmp = -1
        while(len(q)>0):
            v = q.popleft()
            for i in range(4):
                next_x = v[0] + yoko[i]
                next_y = v[1] + tate[i]
                if next_x < 0 or next_x >= H or next_y < 0 or next_y >= W:
                    continue
                if dist[next_x][next_y] == -1 and S[next_x][next_y] == ".":
                    q.append((next_x,next_y))
                    dist[next_x][next_y] = dist[v[0]][v[1]] + 1
                    tmp = max(tmp,dist[next_x][next_y])
        ans = max(tmp,ans)
print(ans)