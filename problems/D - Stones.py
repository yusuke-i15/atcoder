N,K = map(int,input().split())
A = list(map(int,input().split()))
dp = [0]*(N+1)
for i in range(1,N+1):
    for j in A:
        if j > i:
            break
        dp[i] = max(dp[i],j+(i-j)-dp[(i-j)])
print(dp[N])
N = int(input())
