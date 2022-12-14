from collections import defaultdict
N,M = map(int,input().split())
dic = defaultdict(lambda :1)
ans = defaultdict(int)
ans[1] = 1
for i in range(M):
    x,y = map(int,input().split())
    dic[x] -= 1
    dic[y] += 1
    if ans[x] == 1:
        ans[y] = 1
    if dic[x] == 0:
        ans[x] = 0
cnt = 0
for i in ans:
    if ans[i] == 1:
        cnt += 1
print(cnt)