N = int(input())
a = [int(input()) for i in range(N)]
ans = 0
for i in range(N-1):
    if a[i]%2 == 1:
        if a[i+1] == 0:
            continue
        else:
            ans += 1
            a[i+1] -= 1
for i in range(N):
    ans += a[i]//2    
print(ans)