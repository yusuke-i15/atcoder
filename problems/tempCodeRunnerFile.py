n,m = map(int,input().split())

s = [0]*(n+1)
for i in range(n-1):
    temp = int(input())
    s[i+1] = s[i] + temp

start = 0
ans = 0
for i in range(m):
    q = int(input())
    ans += abs(s[q+start]-s[start])
    start = q+start
print(ans)