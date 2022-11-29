from collections import defaultdict
N,M = map(int,input().split())
dic = defaultdict(int)
ab = [tuple(map(int,input().split())) for i in range(M)]
for a,b in ab:
    if a == 1:
        dic[b] += 1
    if b == 1:
        dic[a] += 1
flag = False
for a,b in ab:
    if a == N and dic[b] >= 1:
        flag = True
    if b == N and dic[a] >= 1:
        flag = True
print("POSSIBLE" if flag else "IMPOSSIBLE")