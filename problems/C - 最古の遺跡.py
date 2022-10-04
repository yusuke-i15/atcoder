from itertools import combinations
from collections import defaultdict
N = int(input())

S = []
for i in range(N):
    S.append(tuple(map(int,input().split())))
S = sorted(S)
set_S = set(S)
print(set_S)
comb = combinations(S,2)
result = 0
for i in comb:
    x1,y1 = i[0]
    x2,y2 = i[1]
    q = (x2-y2+y1,y2+x2-x1)
    r = (x1-y2+y1,y1+x2-x1)
    if q in set_S  and r in set_S:
        result = max(result,(x2-x1)**2+(y2-y1)**2)
print(result)

"""
dic_S = defaultdict(int)
for i in range(N):
    dic_S[tuple(map(int,input().split()))] = 1
comb = combinations(dic_S,2)
comb = sorted(comb)
result = 0
for i in comb:
    x1,y1 = i[0]
    x2,y2 = i[1]
    q = (x2-y2+y1,y2+x2-x1)
    r = (x1-y2+y1,y1+x2-x1)
    if dic_S[q] == 1  and dic_S[r] == 1:
        result = max(result,(x2-x1)**2+(y2-y1)**2)
print(result)
print(dic_S)
"""