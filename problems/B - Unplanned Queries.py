from collections import defaultdict
N,M = map(int,input().split())
dic = defaultdict(int)
for i in range(M):
    a,b = map(int,input().split())
    dic[a] += 1
    dic[b] += 1
flag = True
for i in range(1,N+1):
    if dic[i]%2 != 0:
        flag = False
print("YES" if flag else "NO")