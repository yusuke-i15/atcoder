import sys
sys.setrecursionlimit(10**9)
tate = [1,0,-1,0,1,1,-1,-1]
yoko = [0,1,0,-1,1,-1,1,-1]

def dfs(x,y):
    c[x][y] = 0
    for i in range(-1,2,1):
        for j in range(-1,2,1):
            xn = x + i
            yn = y + j
            if xn >= 0 and xn <= h-1 and yn >= 0 and yn <= w-1:
                if c[xn][yn] == 1:
                    dfs(xn,yn)
ans = []
while True:
    w,h = map(int,input().split())
    if w == 0:
        break
    #c = [list(map(int,input().split())) for i in range(h)]
    c = [list(map(int, input().split())) for _ in range(h)]
    count = 0
    for i in range(h):
        for j in range(w):
            if c[i][j] == 1:
                count += 1
                dfs(i,j)
    ans.append(count)
    
for i in ans:
    print(i)