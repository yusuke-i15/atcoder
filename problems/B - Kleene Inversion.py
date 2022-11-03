N,K = map(int,input().split())
A = list(map(int,input().split()))
mod = 10**9+7
ans = 0
for i in range(N):
    temp = 0
    ij = 0
    for j in range(N):
        if A[i] > A[j]:
            temp += 1
            if i>j:
                ij += 1
    ans += temp*K*(K+1)//2 -ij*K
    ans = ans%mod
print(ans)