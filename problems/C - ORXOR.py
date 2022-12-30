from itertools import product
N = int(input())
A = list(map(int,input().split()))
ans = float("inf")
for pro in product((0,1),repeat=N-1):
    tmp = A[0]
    v = 0
    for i in range(N-1):
        if pro[i] == 0:
            tmp |= A[i+1]
        else:
            v ^= tmp
            tmp = A[i+1]
    ans = min(ans,v^tmp)
print(ans)