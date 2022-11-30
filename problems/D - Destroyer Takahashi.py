N,D = map(int,input().split())
lr = [tuple(map(int,input().split())) for i in range(N)]
lr = sorted(lr,key = lambda x:x[1])
ans = 1
tmp = lr[0][1]
i = 1
while(i<N):
    l,r = lr[i]
    if l > tmp+D -1:
        tmp = r
        ans += 1
    i += 1
print(ans)