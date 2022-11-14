N = int(input())
a = list(map(int,input().split()))
b = [0]*N
for i in range(N,0,-1):
    tmp = 2
    count = 0
    while(tmp*i <= N):
        count += b[tmp*i-1]
        tmp += 1
    if count%2 == 0:
        b[i-1] = a[i-1]
    else:
        if a[i-1] == 0:
            b[i-1] = 1
cnt = 0
ans = []
for i in range(N):
    if b[i] != 0:
        cnt += 1
        ans.append(i+1)
print(cnt)
print(*ans)