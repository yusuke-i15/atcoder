import collections
from collections import deque
N = int(input())
A = list(map(int,input().split()))
A.sort()
c = collections.Counter(A)
# [('a', 4), ('c', 2), ('b', 1)]
q = deque()
amari = 0
ans = 0
for i in c:
    q.append(i)
    amari += c[i]-1

for i in range(1,N+1):
    if q[0] != i:
        if amari >= 2:
            amari -= 2
        elif amari == 1:
            amari = 0
            q.pop()
        else:
            if len(q) < 2:
                ans = i-1
                break
            q.pop()
            q.pop()
    else:
        q.popleft()
    if len(q) == 0:
        ans = i+amari//2
        break
print(ans)