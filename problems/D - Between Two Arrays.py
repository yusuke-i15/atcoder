mod = 998244353
N = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
ans = 0
dp = [1]*(3001)
for i in range(N):
    nx = [0]*(3001)
    for j in range(a[i],b[i]+1):
        nx[j] = dp[j]
    dp = nx
    for i in range(3000):
        dp[i+1] += dp[i]
        dp[i+1] %= mod
print(dp[3000])