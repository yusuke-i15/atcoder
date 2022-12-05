from collections import defaultdict
N = int(input())
S = input()
mod = 10**9 + 7
dic = defaultdict(int)
for i in S:
    dic[i] += 1
ans = 1
for i in dic:
    ans *= (dic[i]+1)
    ans %= mod
print(ans-1)