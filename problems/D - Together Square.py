N = int(input())
ans = 0
for i in range(1,N+1):
    k = i
    d = 2
    while(d**2<=k):
        while(k%(d**2)==0):
            k = k//d**2
        d += 1
    d = 1
    while(k*d*d<=N):
        ans += 1
        d += 1
print(ans)