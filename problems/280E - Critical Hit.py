N,P = map(int,input().split())
mod = 998244353
P = P*pow(100,-1,mod)%mod
dp = [0]*(N+1)
dp[1] = 1
for i in range(2,N+1):
    dp[i] = 1 + dp[i-2]*P + dp[i-1]*(1-P)
    dp[i] %= mod
print(dp[N])