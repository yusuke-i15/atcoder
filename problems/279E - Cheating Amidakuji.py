from collections import defaultdict
N,M = map(int,input().split())
A = list(map(int,input().split()))
dic = defaultdict(int)
B = list(range(N+1))
for i in range(M):
    tmp = B[A[i]]
    B[A[i]] = B[A[i]+1]
    B[A[i]+1] = tmp
for i in range(1,N+1):
    dic[B[i]] = i
B_tmp = list(range(N+1))
for i in range(M):
    if B_tmp[A[i]] == 1:
        print(dic[B_tmp[A[i]+1]])
    elif B_tmp[A[i]+1] == 1:
        print(dic[B_tmp[A[i]]])
    else:
        print(dic[1])
    tmp = B_tmp[A[i]]
    B_tmp[A[i]] = B_tmp[A[i]+1]
    B_tmp[A[i]+1] = tmp