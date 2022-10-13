import sys
sys.setrecursionlimit(10**9)

m = int(input())
n = int(input())
c = [list(map(int,input().split())) for i in range(n)]

tate = [1,0,-1,0]
yoko = [0,1,0,-1]
"""
def dfs(seen,h,w,count,his):
    seen[h][w] = 1
    count += 1
    his.append(count)
    for i in range(4):
        h_next = h + tate[i]
        w_next = w + yoko[i]
        if h_next >=0 and h_next < n and w_next >= 0 and w_next < m:
            if c[h_next][w_next] == 1 and seen[h_next][w_next] != 1:
                dfs(seen,h_next,w_next,count,his)
    count -= 1
"""
def dfs(h,w,count,his):
    c[h][w] = 0
    count += 1
    his.append(count)
    for i in range(4):
        h_next = h + tate[i]
        w_next = w + yoko[i]
        if h_next >=0 and h_next < n and w_next >= 0 and w_next < m:
            if c[h_next][w_next] == 1:
                dfs(h_next,w_next,count,his)
    c[h][w] = 1
ans = 0
for i in range(n):
    for j in range(m):
        if c[i][j] == 1:
            his = []
            dfs(i,j,0,his)
            ans = max(ans,max(his))
print(ans)