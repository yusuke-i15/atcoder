from collections import defaultdict
from collections import deque

H,W = map(int,input().split())
S = list(input() for i in range(H))

dist = defaultdict(lambda: defaultdict(lambda: -1))
q = deque()
q.append((0,0))
dist[0][0] = 0
tate = [1,-1,0,0]
yoko = [0,0,1,-1]
tateh = []
yokoh = []
while(len(q)>0):
    v = q.popleft()
    for i in range(4):
        next_x = v[0] + yoko[i]
        next_y = v[1] + tate[i]
        #番兵法ないとき
        if next_x < 0 or next_x >= H or next_y < 0 or next_y >= W:
            continue
        if dist[next_x][next_y] == -1 and S[next_x][next_y] == ".":
            q.append((next_x,next_y))
            dist[next_x][next_y] = dist[v[0]][v[1]] + 1
        if S[next_x][next_y] == "#":
            if i <= 1:
                tateh.append((next_x,next_y,i))
            else:
                yokoh.append((next_x,next_y,i))
ans = 0
seen = defaultdict(lambda: -1)
for ix,iy,i in tateh:
    if seen[(ix,iy,i)] == -1:
        ans += 1
        tmpx = ix
        tmpy = iy
        while((tmpx,tmpy,i) in tateh):
            seen[(tmpx,iy,i)] = 1
            tmpx += 1
        tmpx = ix
        while((tmpx,tmpy,i) in tateh):
            seen[(tmpx,iy,i)] = 1
            tmpx -= 1
seen = defaultdict(lambda: -1)
for ix,iy,i in yokoh:
    if seen[(ix,iy,i)] == -1:
        ans += 1
        tmpx = ix
        tmpy = iy
        while((tmpx,tmpy,i) in yokoh):
            seen[(ix,tmpy,i)] = 1
            tmpy += 1
        tmpy = iy
        while((tmpx,tmpy,i) in yokoh):
            seen[(ix,tmpy,i)] = 1
            tmpy -= 1
print(ans)