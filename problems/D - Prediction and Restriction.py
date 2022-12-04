N,K = map(int,input().split())
R,S,P = map(int,input().split())
T = list(input())
dp = [[0]*(N) for i in range(3)]
rsp = ["r","s","p"]
ans = 0
for i in range(N):
    if i-K >= 0 and T[i-K] == T[i]:
        T[i] = "f"
        continue
    if T[i] == "r":
        ans += P
    if T[i] == "s":
        ans += R
    if T[i] == "p":
        ans += S
print(ans)