H,W = map(int,input().split())
S = [["#"]*(W+2) for i in range(H+2)]
for i in range(1,H+1):
    S[i][1:W+1] = input()

l = [[0]*(W+2) for i in range(H+2)]
u = [[0]*(W+2) for i in range(H+2)]
sets = []
for i in range(H+2):
    for j in range(W+2):
        if S[i][j] == ".":
            tmp += 1
            sets.append((i,j))
        else:
            for h,w in sets:
                l[h][w] = tmp
            sets = []
            tmp = 0
for i in range(W+2):
    for j in range(H+2):
        if S[j][i] == ".":
            tmp += 1
            sets.append((j,i))
        else:
            for h,w in sets:
                u[h][w] = tmp
            sets = []
            tmp = 0
ans = 0
for i in range(H+2):
    for j in range(W+2):
        ans = max(ans,l[i][j]+u[i][j]-1)
print(ans)