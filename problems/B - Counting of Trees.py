from collections import defaultdict
N = int(input())
D = list(map(int,input().split()))
mod = 998244353
dic = defaultdict(int)
for i in D:
    dic[i] += 1
if dic[0] >= 2 or D[0] != 0:
    print(0)
else:
    ans = 1
    for i in range(1,N):
        ans = ans*dic[i-1]**dic[i]
        ans = ans%mod
    print(ans)