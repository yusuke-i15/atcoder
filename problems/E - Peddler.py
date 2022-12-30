N,M = map(int,input().split())
A = list(map(int,input().split()))
XY = [list(map(int,input().split())) for i in range(M)]
XY.sort(key=lambda x:x[1])
maN = [0]*N
miN = [0]*N
for i in range(N):
    maN[i] = A[i]
    miN[i] = A[i]
ans = -float("inf")
for x,y in XY:
    x -= 1
    y -= 1
    ans = max(ans,A[y]-miN[x])
    miN[y] = min(miN[y],miN[x])
print(ans)