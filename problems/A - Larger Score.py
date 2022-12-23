N,K = map(int,input().split())
A = list(map(int,input().split()))
dic = []
for i in range(N):
    dic.append((A[i],-i))
dic = sorted(dic)
ans = float("inf")
tmp = -float("inf")
for a,mi in dic:
    i = -mi
    if i >= K:
        ans = min(ans,i-tmp)
    else:
        tmp = max(tmp,i)
if ans < float("inf"):
    print(ans)
else:
    print(-1)