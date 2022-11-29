N,C,K = map(int,input().split())
T = [int(input()) for i in range(N)]
T.sort()
ans = 0
i = 0
while(i<N):
    tmp = T[i]
    cnt = 1
    ans += 1
    if i + 1 >= N:
        break
    while(T[i+1] <= tmp + K):
        if cnt + 1 > C:
            break
        cnt += 1
        i += 1
        if i+1 >= N:
            break
    i += 1
print(ans)