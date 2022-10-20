N,M = map(int,input().split())
l = 0
r = float("inf")
for i in range(M):
    L,R = map(int,input().split())
    l = max(l,L)
    r = min(r,R)
if r>=l:
    print(r-l+1)
else:
    print(0)