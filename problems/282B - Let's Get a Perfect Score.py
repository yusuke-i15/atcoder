import itertools
N,M = map(int,input().split())
S = [input() for i in range(N)]
c = itertools.combinations(range(N),2)
ans = 0
for i1,i2 in c:
    flag = True
    for i in range(M):
        if S[i1][i] == "x" and S[i2][i] == "x":
            flag = False
    if flag:
        ans += 1
print(ans)