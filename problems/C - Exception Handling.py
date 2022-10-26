from collections import defaultdict
N = int(input())
A = list(int(input()) for i in range(N))
dic = defaultdict(int)
for i in range(N):
    dic[i] = A[i]
A.sort()
for i in range(N):
    if A[-1] == dic[i]:
        print(A[-2])
    else:
        print(A[-1])