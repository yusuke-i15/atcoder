N,K = map(int,input().split())
A = list(map(int,input().split()))
for i in range(101):
    A.append(0)
ans = []
for i in range(K,K+N):
    ans.append(A[i])
print(*ans)