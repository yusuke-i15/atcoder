H,W = map(int,input().split())
C = list(input() for i in range(H))
ans = []
for i in range(W):
    count = 0
    for j in range(H):
        if C[j][i] == "#":
            count += 1
    ans.append(count)
print(*ans)