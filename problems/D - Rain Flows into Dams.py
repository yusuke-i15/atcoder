N = int(input())
A = list(map(int,input().split()))
ans = [0]*N
for i in range(0,N,2):
    ans[0] += A[i]
for i in range(1,N,2):
    ans[0] -= A[i]
for i in range(1,N):
    ans[i] = 2*A[i-1] - ans[i-1]
print(*ans)