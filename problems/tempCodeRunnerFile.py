    X.sort()
    dis = [0]*(M-1)
    for i in range(M-1):
        dis[i] = X[i+1]-X[i]
    dis.sort()
    ans = sum(dis)
    for i in range(N-1):
        ans -= dis[-(i+1)]
    print(ans)