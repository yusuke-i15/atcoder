from collections import defaultdict
N = int(input())
A = list(map(int,input().split()))
dic = defaultdict(int)
for i in range(N):
    dic[A[i]] = i
used = defaultdict(int)
ans = []
flag = True
for i in range(1,N+1):
    start = dic[i]
    for j in range(start,i-1,-1):
        if used[j] == 1:
            flag = False
            break
        else:
            used[j] += 1
            ans.append(j)
            dic[A[j-1]] += 1
if flag and len(ans) == N-1:
    for i in ans:
        print(i)
else:
    print(-1)