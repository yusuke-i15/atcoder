N = int(input())
dp = [0]*(10**5+2)
six = 1
nine = 1
for i in range(1,N+1):
    if i >= six*6:
        six = six*6
    if i >= nine*9:
        nine = nine*9
    dp[i] = min(i,dp[i-six]+1,dp[i-nine]+1)
print(dp[N])
