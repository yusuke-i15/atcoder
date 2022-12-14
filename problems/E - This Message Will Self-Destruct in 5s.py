import collections
N = int(input())
A = list(map(int,input().split()))
for i in range(N):
    A[i] = A[i] - i
C = collections.Counter(A)
# [('a', 4), ('c', 2), ('b', 1)]
tmp = 0
ans = 0
for j in range(N):
    ans += C[-A[j]-tmp]
    tmp += 2
print(ans)