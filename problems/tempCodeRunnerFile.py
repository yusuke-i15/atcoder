<<<<<<< HEAD
N,T = map(int,input().split())
t = list(map(int,input().split()))
ans = 0
for i in range(N-1):
    ans += min(T,t[i+1]-t[i])
ans += T
print(ans)
=======
    X.sort()
    dis = [0]*(M-1)
    for i in range(M-1):
        dis[i] = X[i+1]-X[i]
    dis.sort()
    ans = sum(dis)
    for i in range(N-1):
        ans -= dis[-(i+1)]
    print(ans)
>>>>>>> 3bb5dc0fc6fa090698c8c7ea95eae5382cbd41a2
