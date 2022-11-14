def factorize(n):
    n_root = int(n**0.5)
    facto = []
    for i in range(2,n_root+1):
        while(n%i == 0):
            facto.append(i)
            n = n//i
    if n != 1:
        facto.append(n)
    return facto

from collections import defaultdict
N = int(input())
dic =defaultdict(int)
mod = 10**9 + 7
for i in range(2,N+1):
    tmp = factorize(i)
    for j in tmp:
        dic[j] += 1
ans = 1
for i in dic:
    ans = ans*(dic[i]+1)
    ans = ans %mod
print(ans)