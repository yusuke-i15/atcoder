from collections import defaultdict
N,M = map(int,input().split())
X = list(map(int,input().split()))
dic = defaultdict(int)
for i in range(M):
    c,y = map(int,input().split())
    dic[c] = y
dp = [[0]*(N+2) for i in range(N+1)]
for i in range(1,N+1):
    for j in range(1,i+1):
        dp[i][j] = dp[i-1][j-1] + X[i-1] + dic[j]
    dp[i][0] = max(dp[i-1])
print(max(dp[N]))