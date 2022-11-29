from collections import defaultdict
N = int(input())
a = list(map(int,input().split()))
dic = defaultdict(int)
for i in a:
    dic[i] += 1
ans = 0
for i in dic:
    if dic[i] < i:
        ans += dic[i]
    else:
        ans += dic[i] - i
print(ans)