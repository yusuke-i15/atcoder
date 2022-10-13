from collections import deque

H,W = map(int,input().split())
S = [list(input()) for i in range(H)]

dist = [[0]*W for i in range(H)]
dist[0][0] = 1
q = deque()
q.append((0,0))
tate = [1,0,-1,0]
yoko = [0,1,0,-1]
while(len(q)>0):
    v = q.popleft()
    for i in range(4):
        next_x = v[0] + yoko[i]
        next_y = v[1] + tate[i]
        if next_x >= 0 and next_x <= W-1 and next_y >= 0 and next_y <=H-1:
            if dist[next_y][next_x] == 0 and S[next_y][next_x]== ".":
                q.append((next_x,next_y))
                dist[next_y][next_x] = dist[v[1]][v[0]] + 1
if dist[H-1][W-1] == 0:
    print(-1)
else:
    count = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == ".":
                count += 1
    print(count - dist[H-1][W-1])
"""
3 5
.#...
...#.
####.
"""