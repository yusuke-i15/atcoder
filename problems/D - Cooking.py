N = int(input())
T = list(map(int,input().split()))
dp = [[0]*(10**5 + 1) for i in range(N+1)]
dp[0][0] = 1
for i in range(1,N+1):
    for j in range(10**5+1 - T[i-1]):
        if dp[i-1][j] == 1:
            dp[i][j+T[i-1]] = 1
            dp[i][j] = 1
    dp[i][0] = 1
sum_T = sum(T)
tmp = sum_T//2
i = 0
while(True):
    if dp[N][tmp+i] == 1:
        print(max(tmp+i,sum_T - tmp-i))
        break
    if dp[N][tmp-i] == 1:
        print(max(tmp-i,sum_T - tmp + i))
        break
    i += 1