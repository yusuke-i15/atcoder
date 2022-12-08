N = int(input())
dp = [[0]*(7) for i in range(10**5+1)]
txa = [tuple(map(int,input().split())) for i in range(N)]
tmp = 0
t,x,a = txa[0]
for i in range(1,10**5+1):
    for j in range(1,6):
        dp[i][j] = max(dp[i-1][j-1],dp[i-1][j],dp[i-1][j+1])
    if i == t:
        tmp += 1
        if x <= i:
            dp[t][x+1] += a
        t,x,a = txa[min(tmp,N-1)]
print(max(dp[10**5]))