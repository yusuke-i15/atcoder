from itertools import product
N = int(input())
F = [list(map(int,input().split())) for i in range(N)]
P = [list(map(int,input().split())) for i in range(N)]
ans = -float("inf")
for pro in product((0,1),repeat = 10):
    if sum(pro) == 0:
        continue
    p = 0
    for i in range(N):
        ci = 0
        for j in range(10):
            if pro[j] == 1 and F[i][j] == 1:
                ci += 1
        p += P[i][ci]
    ans = max(ans,p)
print(ans)