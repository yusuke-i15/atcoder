N,K = map(int,input().split())
a = list(map(int,input().split()))

r = 0
ans = 0
sum_tmp = 0
for i in range(N):
    while(r<=N):
        if sum_tmp >= K:
            ans += N-r+1
            break
        if r==N:
            break
        sum_tmp += a[r]
        r += 1
    sum_tmp -= a[i]
print(ans)