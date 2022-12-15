N = int(input())
yaku = [1]*(N+1)
for i in range(2,N+1):
    for j in range(i,N+1,i):
        yaku[j] += 1
ans = 0
for i in range(1,N+1):
    ans += i*yaku[i]
print(ans)