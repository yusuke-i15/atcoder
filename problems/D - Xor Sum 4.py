mod = 10**9 + 7
N = int(input())
A = list(map(int,input().split()))

ans = 0
for i in range(61):
    tmp = 0
    for j in A:
        if j>>i&1 == 1:
            tmp += 1
    ans += tmp*(N-tmp)*2**i
    ans%mod
print(ans%mod)