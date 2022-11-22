N,K = map(int,input().split())
ans = 0
if K == 0:
    ans = N**2
else:
    for i in range(K+1,N+1):
        tmp = N//i
        ans += (i-K)*tmp
        l = K + i*tmp
        if l <= N:
            ans += N - l+1
print(ans)