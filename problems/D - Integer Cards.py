from collections import defaultdict
N,M = map(int,input().split())
A = list(map(int,input().split()))
dic = defaultdict(int)
for i in range(M):
    b,c = map(int,input().split())
    dic[c] += b
dic = dict(sorted(dic.items(),reverse=True))
A.sort()
okikae = []
for k,v in dic.items():
    for j in range(v):
        if len(okikae) < N:
            okikae.append(k)
        else:
            break
    if len(okikae) >N:
        break
tmp = 0
for i in okikae:
    if A[tmp] < i:
        A[tmp] = i
        tmp += 1
print(sum(A))