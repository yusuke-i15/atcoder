H,W = map(int,input().split())
A = [input() for i in range(H)]
tmp_W = 0
flag = True
cnt = 0
for i in range(H):
    for j in range(W):
        if A[i][j] == "#":
            cnt += 1 
for i in range(H):
    if A[i][tmp_W] != "#":
        flag = False
    while(tmp_W+1 < W and A[i][tmp_W+1] == "#"):
        tmp_W += 1
if tmp_W != W-1 or cnt > H+W-1:
    flag = False
print("Possible" if flag else "Impossible")