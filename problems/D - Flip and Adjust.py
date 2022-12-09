N,S = map(int,input().split())
dp = [["N"]*(10**4+1) for i in range(N+1)]
dp[0][0] = "S"
for i in range(1,N+1):
    a,b = map(int,input().split())
    for j in range(10**4+1):
        if dp[i-1][j] == "S":
            dp[i][j+a] = "H"
            dp[i][j+b] = "T"
        elif dp[i-1][j] != "N":
            dp[i][j+a] = dp[i-1][j] + "H"
            dp[i][j+b] = dp[i-1][j] + "T"
if dp[N][S] == "N":
    print("No")
else:
    print("Yes")
    print(dp[N][S])