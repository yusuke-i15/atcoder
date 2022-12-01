from collections import defaultdict
N = int(input())
dic = defaultdict(int)
A = list(map(int,input().split()))
sets = set(A)
for i in A:
    dic[i] += 1
ans = 0

for i in sets:
    for j in range(1,int(i**0.5)+1):
        if i%j == 0:
            if i//j == j:
                ans += dic[i]*dic[j]*dic[j]
            else:
                ans += dic[i]*dic[j]*dic[i//j]*2
print(ans)