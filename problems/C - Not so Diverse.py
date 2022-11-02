from collections import defaultdict
N,K = map(int,input().split())
A = list(map(int,input().split()))

dic = defaultdict(int)
for i in A:
    dic[i] += 1
if len(dic) <= K:
    print(0)
else:
    dic = sorted(dic.values())
    ans = 0
    for i in range(len(dic)-K):
        ans += dic[i]
    print(ans)