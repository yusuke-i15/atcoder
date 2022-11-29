N = int(input())
A = list(map(int,input().split()))
A = [0] + A + [0]
ans = 0
for i in range(N+1):
    ans += abs(A[i]-A[i+1])
for i in range(1,N+1):
    print(ans - abs(A[i]-A[i-1]) - abs(A[i]-A[i+1]) + abs(A[i-1]-A[i+1]))