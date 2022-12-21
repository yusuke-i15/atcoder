import itertools
N,M,Q = map(int,input().split())
abcd = [tuple(map(int,input().split())) for i in range(Q)]
com = itertools.combinations_with_replacement(range(1,M+1),N)
ans = 0
for A in com:
    tmp = 0
    for i in range(Q):
        a,b,c,d = abcd[i]
        if A[b-1] - A[a-1] == c:
            tmp += d
    ans = max(ans,tmp)
print(ans)