H,W = map(int,input().split())
S = [["."]*(W+2) for _ in range(H+2)]
for i in range(1,H+1):
    S[i][1:W+1] = input()
ans = [[""]*W for i in range(H)]
tate = [-1,-1,-1,0,1,1,1,0]
yoko = [-1,0,1,1,1,0,-1,-1]
for i in range(1,H+1):
    for j in range(1,W+1):
        if S[i][j] == "#":
            ans[i-1][j-1] = "#"
        else:
            temp = 0
            for k in range(8):
                if S[i+tate[k]][j+yoko[k]] == "#":
                    temp += 1
            ans[i-1][j-1] = temp
for i in range(H):
    print(*ans[i],sep="")