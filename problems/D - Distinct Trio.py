from collections import defaultdict
N = int(input())
A = list(map(int,input().split()))
dic = defaultdict(int)
for i in A:
    dic[i] += 1
c = dict(sorted(dic.items(),key=lambda x:x[0]))
tmp = 0
ans = 0
for i in c:
    ans += tmp*(N-c[i]-tmp)*c[i]
    tmp += c[i]
print(ans)