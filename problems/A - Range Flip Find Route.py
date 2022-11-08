H,W = map(int,input().split())

S = [input() for i in range(H)]
dp = [[float("inf")]*W for i in range(H)]


dp[0][0] = 0
for i in range(H):
    for j in range(W):
        if i-1 >= 0:
            if S[i-1][j] == "." and S[i][j] == "#":
                dp[i][j] = min(dp[i][j],dp[i-1][j]+1)
            else:
                dp[i][j] = min(dp[i][j],dp[i-1][j])
        if j-1 >= 0:
            if S[i][j-1] == "." and S[i][j] == "#":
                dp[i][j] = min(dp[i][j],dp[i][j-1]+1)
            else:
                dp[i][j] = min(dp[i][j],dp[i][j-1])
if S[0][0] == "#":
    print(dp[H-1][W-1]+1)
else:
    print(dp[H-1][W-1])