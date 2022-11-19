from collections import defaultdict
N = int(input())
A = list(map(int,input().split()))
Q = int(input())
tmp = 0
flag = False
for i in range(Q):
    q = list(map(int,input().split()))
    if q[0] == 1:
        flag = True
        tmp = q[1]
        dic = defaultdict(int)
    elif q[0] == 2:
        if flag:
            dic[q[1]-1] += q[2]
        else:
            A[q[1]-1] += q[2]
    elif q[0] == 3:
        if flag:
            print(dic[q[1]-1] + tmp)
        else:
            print(A[q[1]-1])