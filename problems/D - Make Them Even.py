H,W = map(int,input().split())
a = [list(map(int,input().split())) for i in range(H)]
ans = []
for i in range(H):
    for j in range(W):
        if a[i][j]%2 == 1:
            if j == W-1:
                continue
            ans.append((i+1,j+1,i+1,j+2))
            a[i][j+1] += 1
for i in range(H):
    if a[i][W-1]%2 == 1:
        if i == H-1:
            continue
        ans.append((i+1,W,i+2,W))
        a[i+1][W-1] += 1
N = len(ans)
print(N)
for i in ans:
    print(*i)