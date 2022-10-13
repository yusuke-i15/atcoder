from collections import deque
from collections import defaultdict
import math

N,M = map(int,input().split())
sqM = M**0.5
M_k = math.ceil(sqM)

comb = []
for i in range(M_k+1):
    for j in range(M_k+1):
        if i**2 + j**2 == M:
            comb.append((i,j))

#dist:開始点からの距離_今回はノード0
dist = [[-1]*N for i in range(N)]
dist[0][0] = 0
q = deque()
q.append((1,1))

while(len(q) > 0):
    v = q.popleft()
    x = v[0]
    y = v[1]
    for next in comb:
        nx = x + next[0]
        ny = y + next[1]
        if nx >= 1 and nx <= N and ny >= 1 and ny <= N:
            if dist[nx-1][ny-1] == -1:
                q.append((nx,ny))
                dist[nx-1][ny-1] = dist[x-1][y-1] + 1
        nx = x - next[0]
        ny = y - next[1]
        if nx >= 1 and nx <= N and ny >= 1 and ny <= N:
            if dist[nx-1][ny-1] == -1:
                q.append((nx,ny))
                dist[nx-1][ny-1] = dist[x-1][y-1] + 1
        nx = x - next[0]
        ny = y + next[1]
        if nx >= 1 and nx <= N and ny >= 1 and ny <= N:
            if dist[nx-1][ny-1] == -1:
                q.append((nx,ny))
                dist[nx-1][ny-1] = dist[x-1][y-1] + 1
        nx = x + next[0]
        ny = y - next[1]
        if nx >= 1 and nx <= N and ny >= 1 and ny <= N:
            if dist[nx-1][ny-1] == -1:
                q.append((nx,ny))
                dist[nx-1][ny-1] = dist[x-1][y-1] + 1
for i in range(N):
    print(*dist[i])

