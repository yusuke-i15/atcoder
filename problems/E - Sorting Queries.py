import heapq
from collections import deque
Q = int(input())
ans = []
s = 0
unsort = deque()
for i in range(Q):
    q = list(map(int,input().split()))
    if q[0] == 1: 
        unsort.append(q[1])
    elif q[0] == 2:
        if s == 0:
            ans.append(unsort.popleft())
        else:
            if len(A) == 0:
                ans.append(unsort.popleft())
            else:
                ans.append(heapq.heappop(A))
    else:
        if s == 0:
            A = list(unsort)
            heapq.heapify(A)
            s += 1
        else:
            if len(A) == 0:
                A = list(unsort)
                heapq.heapify(A) 
            else:
                for i in range(len(unsort)):
                    heapq.heappush(A,unsort[i])
        unsort = deque()
for i in ans:
    print(i)