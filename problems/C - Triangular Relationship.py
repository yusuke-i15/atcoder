N,K = map(int,input().split())
tmp1 = 0
tmp2 = 0
for i in range(1,N+1):
    if i%K == 0:
        tmp1 += 1
    if K%2 == 0 and i%K == K//2:
        tmp2 += 1
print(tmp1**3 + tmp2**3)