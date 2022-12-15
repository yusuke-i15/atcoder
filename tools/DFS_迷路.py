import sys
sys.setrecursionlimit(10**9)
from collections import defaultdict
seen = defaultdict(lambda: defaultdict(int))

H,W = map(int,input().split())
C = [input() for i in range(H)]
tate = [1,0,-1,0]
yoko = [0,1,0,-1]
def dfs(h,w):
    seen[h][w] += 1
    for i in range(4):
        h_next = h + tate[i]
        w_next = w + yoko[i]
        if h_next >=0 and h_next < H and w_next >= 0 and w_next < W:
            if C[h_next][w_next] != "#" and seen[h_next][w_next] == 0:
                dfs(h_next,w_next)
for i in range(H):
    for j in range(W):
        if C[i][j] == "s":
            start = (i,j)
        if C[i][j] == "g":
            goal = (i,j)
dfs(start[0],start[1])

if seen[goal[0]][goal[1]] == 1:
    print("Yes")
else:
    print("No")
