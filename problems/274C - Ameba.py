N = int(input())
A = list(map(int,input().split()))
ans = [0]*(2*N+5)
for i in range(1,N+1):
    ans[i*2] = ans[A[i-1]] + 1
    ans[i*2+1] = ans[A[i-1]] + 1
for i in range(1,2*N+2):
    print(ans[i])