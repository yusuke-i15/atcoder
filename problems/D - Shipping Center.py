from collections import defaultdict
N,M,Q = map(int,input().split())
WV = [tuple(map(int,input().split())) for i in range(N)]
X = list(map(int,input().split()))
dic = defaultdict(int)
for i in range(1,M+1):
    dic[i] = X[i-1]
dic = dict(sorted(dic.items(),key = lambda x:x[1]))
for i in range(Q):
    l,r = map(int,input().split())
    ans = 0
    used = []
    for j in dic:
        if j >= l and j <= r:
            continue
        ind = -1
        tmpV = 0
        for k in range(N):
            if WV[k][0] <= dic[j] and WV[k][1] > tmpV and k not in used:
                tmpV = WV[k][1]
                ind = k
        used.append(ind)
        ans += tmpV
    print(ans)
                