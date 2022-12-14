import collections
N = int(input())
A = list(map(int,input().split()))
seen = [0]*(10**6+1)
A.sort()
C = collections.Counter(A)
# [('a', 4), ('c', 2), ('b', 1)]
ans = 0
for i in A:
    if seen[i] == 0:
        if C[i] == 1:
            ans += 1
        for j in range(i,10**6+1,i):
            seen[j] = 1
print(ans)