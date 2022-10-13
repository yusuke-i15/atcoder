D,N = map(int,input().split())
T = [0]*D
for i in range(D):
    T[i] = int(input())
ABC = [list(map(int,input().split())) for i in range(N)]

dp = [[0]*N for i in range(D+1)]
for i in range(D):
    temp = T[i]
    for j in range(N):
        if i == 0:
            if temp >= ABC[j][0] and temp <= ABC[j][1]:
                dp[i+1][j] = dp[i][j]
            else:
                dp[i+1][j] = -1
        elif temp >= ABC[j][0] and temp <= ABC[j][1]:
            for k in range(N):
                if dp[i][k] != -1:
                    dp[i+1][j] = max(dp[i+1][j],dp[i][k]+abs(ABC[k][2]-ABC[j][2]))
        else:
            dp[i+1][j] = -1
print(max(dp[D]))