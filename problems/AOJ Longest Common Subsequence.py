q = int(input())
for i in range(q):
    X = input()
    Y = input()
    dp = [[0]*(len(X)+1) for i in range(len(Y)+1)]
    for i in range(1,len(Y)+1):
        for j in range(1,len(X)+1):
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])
            if X[j-1] == Y[i-1]:
                dp[i][j] = max(dp[i-1][j-1]+1,dp[i][j])
                
    print(dp[len(Y)][len(X)])