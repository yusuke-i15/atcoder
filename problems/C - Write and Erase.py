from collections import defaultdict
N = int(input())
dic = defaultdict(int)
for i in range(N):
    A = input()
    if dic[A] != 0:
        dic[A] = 0
    else:
        dic[A] += 1
ans = 0
for i in dic.values():
    if i > 0:
        ans += 1
print(ans)