import math
N = int(input())
ans = 0
tmp2 = N
for i in range(1,int(N//(math.isqrt(N)+1))+1):
    ans += N//i
for i in range(1,(math.isqrt(N)+1)):
    ans += i*(int(N//i)-int(N//(i+1)))
print(ans)
