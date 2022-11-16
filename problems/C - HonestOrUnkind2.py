from collections import defaultdict
from itertools import product

N = int(input())

dic = defaultdict(list)
for i in range(1,N+1):
    A = int(input())
    for j in range(A):
        x,y = map(int,input().split())
        dic[i].append((x,y))
        
ans = 0
for pro in product((0,1),repeat=N):
    flag = True
    for i in range(N):
        if pro[i] == 1:
            for x,y in dic[i+1]:
                if pro[x-1] != y:
                    flag = False
    if flag:
        ans = max(ans,sum(pro))
print(ans)