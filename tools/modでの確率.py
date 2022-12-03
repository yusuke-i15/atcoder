mod = 10**9 + 7
#pypyだとpow(a,-1,mod)はエラー
#pow(a,mod-2,mod)が無難
#逆元
print(pow(38, -1, mod))
#確率P/Q : RQ=P(mod 998244353)
mod = 998244353
P = 10
P = P*pow(100,-1,mod)%mod
R = P**2
R %= mod
print(R)
#280E- Critical Hit
"""
N,P = map(int,input().split())
mod = 998244353
P = P*pow(100,-1,mod)%mod
dp = [0]*(N+1)
dp[1] = 1
for i in range(2,N+1):
    dp[i] = 1 + dp[i-2]*P + dp[i-1]*(1-P)
    dp[i] %= mod
print(dp[N])
"""