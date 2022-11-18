from collections import defaultdict
N = int(input())
A = list(map(int,input().split()))

dic = defaultdict(int)
ans = 0
rui = [0]*(N+1)
for i in range(N):
    rui[i+1] = rui[i] + A[i]
    dic[rui[i+1]] += 1
for i in dic:
    if dic[i] >= 2:
        ans += dic[i]*(dic[i]-1)//2
    if i == 0:
        ans += dic[i]
print(ans)