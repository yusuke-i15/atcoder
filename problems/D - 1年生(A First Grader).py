N = int(input())
A = list(map(int,input().split()))
dp = [[0]*(21) for i in range(N-1)]
dp[0][A[0]] = 1
for i in range(N-2):
    temp = A[i+1]
    for j in range(21):
        if j - temp >= 0:
            dp[i+1][j-temp] += dp[i][j]
        if j + temp <= 20:
            dp[i+1][j+temp] += dp[i][j]
print(dp[N-2][A[-1]])