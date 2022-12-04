from collections import deque
N = int(input())
A = list(map(int,input().split()))
q = deque(A)
flip = 0
while(len(q) > 0):
    pre = len(q)
    while(len(q) > 0 and q[-1] == flip):
        q.pop()
    if len(q) > 0:
        if q[0] == flip:
            q.popleft()
            flip ^= 1
    if pre == len(q):
        break
if len(q) == 0:
    print("Yes")
else:
    print("No")