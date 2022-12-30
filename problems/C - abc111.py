from collections import defaultdict
N = int(input())
A = list(map(int,input().split()))
dic0 = defaultdict(int)
for i in range(0,N,2):
    dic0[A[i]] += 1
dic0 = list(tuple(sorted(dic0.items(),key = lambda x:x[1],reverse=True)))
dic1 = defaultdict(int)
for i in range(1,N,2):
    dic1[A[i]] += 1
dic1 = list(tuple(sorted(dic1.items(),key = lambda x:x[1],reverse=True)))
if dic0[0][0] != dic1[0][0]:
    ans = N - dic0[0][1] - dic1[0][1]
else:
    dic0.append((-1,0))
    dic1.append((-1,0))
    ans = N - dic0[0][1] - dic1[1][1]
    ans = min(ans,N-dic0[1][1]-dic1[0][1])
print(ans)