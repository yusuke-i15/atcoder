from collections import defaultdict
N = int(input())
dic = defaultdict(int)
xl = []
for i in range(N):
    X,L = map(int,input().split())
    xl.append((X+L,L))
xl.sort(key = lambda x:x[0])

ans = N
i = 1
ans = 1
tmp_r = xl[0][0]
while (i < N):
    xr,l = xl[i]
    if xr-2*l >= tmp_r:
        ans += 1
        tmp_r = xr
    i += 1
print(ans)