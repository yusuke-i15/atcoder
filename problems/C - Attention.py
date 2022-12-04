N = int(input())
S = input()
er = [0]*N
for i in range(N-1,0,-1):
    if S[i] == "E":
        er[i-1] = er[i] + 1
    else:
        er[i-1] = er[i]
wl = 0
ans = float("inf")
for i in range(N):
    ans = min(ans,wl+er[i])
    if S[i] == "W":
        wl += 1
print(ans)