N = int(input())
A = list(map(int,input().split()))
s = [0]*(N+1)
for i in range(N):
    s[i+1] = s[i] + A[i]

for i in range(1,N+1):
    ans = 0
    for j in range(N+1-i):        
        ans = max(ans,s[j+i]-s[j])
    print(ans)