import math

N,K = map(int,input().split())
ans = 0
for i in range(1,N+1):
    if i < K:
        temp = (K-1+i)//i
        ans += 1/(2**math.ceil(math.log(temp,2)))
    else:
        ans += 1
print(ans/N)