from collections import defaultdict
mod = 998244353
H,W = map(int,input().split())
S = [input() for i in range(H)]
dic = defaultdict(set)
for i in range(H):
    for j in range(W):
        dic[(i+j)].add(S[i][j])
ans = 1
for i in dic:
    if "." in dic[i] and len(dic[i]) == 1:
        ans *= 2
        ans %= mod
    if "R" in dic[i] and "B" in dic[i]:
        ans = 0
print(ans)