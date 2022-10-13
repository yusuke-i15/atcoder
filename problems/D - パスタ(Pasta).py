from collections import defaultdict
dic_S = defaultdict(int)

N,K = map(int,input().split())
dp = [[[0]*4 for j in range(4)] for i in range(N+1)]
for i in range(K):
    a,b = map(int,input().split())
    dic_S[a] = b

dp[0][0][0] = 1
for num in range(1,N+1):
    for i in range(4):
        for j in range(4):
            for k in range(1,4):
                if dic_S[num] >= 1:
                    if k != dic_S[num]:
                        continue
                if k != j or j != i:
                    dp[num][j][k] += dp[num-1][i][j]
ans = 0
for i in range(4):
    for j in range(4):
        ans += dp[N][i][j]
ans = ans %10**4
print(ans)