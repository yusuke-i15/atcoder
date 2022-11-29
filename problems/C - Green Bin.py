from collections import defaultdict
N = int(input())
dic = defaultdict(int)
for i in range(N):
    s = list(input())
    s.sort()
    s = "".join(s)
    dic[s] += 1
ans = 0
for i in dic:
    ans += dic[i]*(dic[i]-1)//2
print(ans)