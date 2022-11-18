from collections import defaultdict
N = int(input())
ans = 0
dic = defaultdict(int)
for i in range(1,N+1):
    tmp = str(i)
    if int(tmp[-1]) >= 1:
        dic[(int(tmp[0]),int(tmp[-1]))] += 1
for i in range(1,10):
    for j in range(1,10):
        ans += dic[(i,j)]*dic[(j,i)]
print(ans)