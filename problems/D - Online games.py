from collections import defaultdict
N = int(input())
dic = defaultdict(int)
for i in range(N):
    a,b = map(int,input().split())
    dic[a] += 1
    dic[a+b] -= 1
dic = dict(sorted(dic.items(),key = lambda x:x[0]))
ans = [0]*(N+1)
tmpd = 0
tmpn = 0
for i in dic:
    ans[tmpn] += (i-tmpd)
    tmpn += dic[i]
    tmpd = i
print(*ans[1:])