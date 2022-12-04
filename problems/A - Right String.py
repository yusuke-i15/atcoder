from collections import defaultdict
N,K = map(int,input().split())
S = input()
kouho = [1]
for i in range(2,int(N**0.5)+1):
    if N%i == 0:
        kouho.append(i)
        kouho.append((N//i))
kouho = list(set(kouho))
kouho.sort()
ans = N
for i in kouho:
    tmp = 0
    for j in range(i):
        dic = defaultdict(int)
        for k in range(j,N,i):
            dic[S[k]] += 1
        tmp += N//i - max(dic.values())
        if tmp > K:
            break
    if tmp <= K:
        ans = i
        break
print(ans)