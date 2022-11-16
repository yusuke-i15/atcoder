from collections import deque
K = int(input())
tmp = 0
q = deque()
for i in range(1,10):
    q.append(i)
while(True):
    x = q.popleft()
    tmp += 1
    if tmp == K:
        print(x)
        break
    if x%10 != 0:
        q.append(10*x + x%10 -1)
    q.append(10*x+x%10)
    if x%10 != 9:
        q.append(10*x + x%10 + 1) 