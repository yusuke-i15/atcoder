H,W,N,M = map(int,input().split())
mh = [[0]*(W+1) for i in range(H+1)]
mv = [[0]*(W+1) for i in range(H+1)]
for i in range(N):
    a,b = map(int,input().split())
    mh[a][b] += 1
    mv[a][b] += 1
for i in range(M):
    c,d = map(int,input().split())
    mh[c][d] = -1
    mv[c][d] = -1
for i in range(1,H+1):
    tmp = 0
    for j in range(1,W+1):
        if mh[i][j] == -1:
            tmp = 0
        else:
            tmp += mh[i][j]
            mh[i][j] = tmp
    tmp = 0
    for j in range(W,0,-1):
        if mh[i][j] == -1:
            tmp = 0
        else:
            tmp += mh[i][j]
            mh[i][j] = tmp
for i in range(1,W+1):
    tmp = 0
    for j in range(1,H+1):
        if mv[j][i] == -1:
            tmp = 0
        else:
            tmp += mv[j][i]
            mv[j][i] = tmp
    tmp = 0
    for j in range(H,0,-1):
        if mv[j][i] == -1:
            tmp = 0
        else:
            tmp += mv[j][i]
            mv[j][i] = tmp
ans = 0
for i in range(1,H+1):
    for j in range(1,W+1):
        if mv[i][j] > 0 or mh[i][j] > 0:
            ans += 1
print(ans)