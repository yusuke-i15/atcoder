N = int(input())
A = list(map(int,input().split()))
A.sort()
rui = [0]*(N+1)
for i in range(N):
    rui[i+1] = rui[i] + A[i]
ans = 1
for i in range(N-1,-1,-1):
    if rui[i]*2 >= A[i]:
        ans += 1
    else:
        break
print(ans)