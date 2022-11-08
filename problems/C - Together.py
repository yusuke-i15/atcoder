from collections import defaultdict
N = int(input())
a = list(map(int,input().split()))
dic = defaultdict(int)
for i in a:
    dic[i] += 1
ans = 0
for i in range(1,10**5):
    ans = max(ans,dic[i-1]+dic[i]+dic[i+1])
print(ans)