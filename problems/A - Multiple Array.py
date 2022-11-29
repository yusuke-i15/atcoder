N = int(input())
A = [0]*N
B = [0]*N
for i in range(N):
    A[i],B[i] = map(int,input().split())
ans = 0
for i in range(N-1,-1,-1):
    if (A[i]+ans)%B[i] != 0:
        ans += B[i] - (A[i]+ans)%B[i]
print(ans)