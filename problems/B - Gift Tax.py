N,a,b = map(int,input().split())
A = list(map(int,input().split()))
l = min(A)
r = max(A)
while(r-l > 1):
    mid = (l+r)//2
    tmp = 0
    for i in range(N):
        if A[i] >= mid:
            tmp += (A[i]-mid)//b
        else:
            tmp -= (mid - A[i]+a-1)//a
    if tmp < 0:
        r = mid
    else:
        l = mid
print(l)