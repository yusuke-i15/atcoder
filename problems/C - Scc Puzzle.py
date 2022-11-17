N,M = map(int,input().split())
ans = 0
if 2*N <= M:
    ans += N
    M = M-2*N
    ans += M//4
    print(ans)
else:
    print(M//2)