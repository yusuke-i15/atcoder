from collections import defaultdict
N = int(input())
S = input()
dic = defaultdict(int)
cnt = 0
for i in range(N-1,-1,-1):
    dic[i] = cnt
    if S[i] == ".":
        cnt += 1
ans = float("inf")
cnt = 0
for i in range(N):
    ans = min(ans,cnt+dic[i])
    if S[i] == "#":
        cnt += 1
print(ans)