N,M = map(int,input().split())
ans = -1
for i in range(1,10):
    d = 0
    for j in range(1,N+1):
        amari = (i + d*10)%M
        if amari == 0:
            ans = max(ans,j*10+i)
        d = amari
if ans != -1:
    print(str(ans%10)*(ans//10))
else:
    print(-1)