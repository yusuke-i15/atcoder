N,Y = map(int,input().split())

ans = [-1,-1,-1]
for i in range(N+1):
    for j in range(N-i+1):
        if (N-i-j)*1000 + i*10000 + j*5000 == Y:
            ans[0] = i
            ans[1] = j
            ans[2] = N-i-j 
print(*ans)