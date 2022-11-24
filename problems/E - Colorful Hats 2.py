from collections import defaultdict
mod = 10**9 + 7
N = int(input())
A = list(map(int,input().split()))
ans = 1
dic = defaultdict(int)
dic[-1] = 3
for i in A:
    ans = ans*dic[i-1]
    dic[i-1] -= 1
    dic[i] += 1
    ans = ans%mod
print(ans)