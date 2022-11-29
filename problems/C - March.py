from collections import defaultdict
from itertools import combinations
N = int(input())
dic = defaultdict(int)
comb = combinations(["M","A","R","C","H"],3)
for i in range(N):
    S = input()
    if S[0] == "M":
        dic["M"] += 1
    if S[0] == "A":
        dic["A"] += 1
    if S[0] == "R":
        dic["R"] += 1
    if S[0] == "C":
        dic["C"] += 1
    if S[0] == "H":
        dic["H"] += 1
ans = 0
for i1,i2,i3 in comb:
    ans += dic[i1]*dic[i2]*dic[i3]
print(ans)