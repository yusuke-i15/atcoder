import heapq
from collections import defaultdict
N,M = map(int,input().split())
AB = [tuple(map(int,input().split())) for i in range(M)]
dic_b = defaultdict(list)
dic_a = defaultdict(int)
AB = list(set(AB))
for a,b in AB:
    dic_a[b] += 1
    dic_b[a].append(b)
A = []
for i in range(1,N+1):
    if dic_a[i] == 0:
        A.append(i)  
heapq.heapify(A)
ans = []
while(len(A) != 0):
    tmp = heapq.heappop(A)
    ans.append(tmp)
    for i in dic_b[tmp]:
        dic_a[i] -= 1
        if dic_a[i] == 0:
            heapq.heappush(A,i)
if len(ans) == N:
    print(*ans)
else:
    print(-1)
    