N = int(input())
ans = 0
for i in range(1,int(N**0.5)+1):
    if N%i == 0:
        tmp = N//i - 1
        if tmp <= 0:
            continue
        if N//tmp == N%tmp:
            ans += tmp
print(ans)