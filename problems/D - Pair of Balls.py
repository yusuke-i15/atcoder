from collections import defaultdict
from collections import deque

N,M = map(int,input().split())
A = [[0] for i in range(M)]
b = [0]*M
for i in range(M):
    k = int(input())
    A[i] = deque(list(map(int,input().split())) + [-1])
seen = defaultdict(lambda: -1)
m = range(M)

while(True):
    m2 = []
    for h in m:
        if seen[A[h][0]] != -1:
            tmp = A[h][0]
            del A[h][0]
            if A[h][0] != -1:
                m2.append(h)
            if A[seen[tmp]][0] != -1:
                m2.append(seen[tmp])
        else:
            seen[A[h].popleft()] = h
    m = m2
    if len(m2) == 0:
        break
flag = True
for i in range(M):
    if A[i][0] != -1:
        flag = False
print("Yes" if flag else "No")