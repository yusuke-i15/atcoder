from collections import defaultdict
N,X,Y = map(int,input().split())
ans = defaultdict(int)
for i in range(1,N):
    for j in range(i+1,N+1):
        dis = min(j-i,abs(X-i)+1+abs(j-Y))
        ans[dis] += 1
for i in range(1,N):
    print(ans[i])