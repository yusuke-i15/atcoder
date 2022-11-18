from itertools import permutations

N = int(input())

xy = [list(map(int,input().split())) for i in range(N)]

P = permutations(range(N),N)
from itertools import product
two = product([0, 1], repeat=4)
temp = 0
count = 0
for i in P:
    pre = i[0]
    for j in range(1,N):
        dis = ((xy[i[j]][0]-xy[pre][0])**2 + (xy[i[j]][1]-xy[pre][1])**2)**0.5
        temp += dis
        pre = i[j]
    count += 1
print(temp/count)