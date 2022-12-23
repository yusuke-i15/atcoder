N,M,K = map(int,input().split())

flag = False
for i in range(N+1):
    for j in range(M+1):
        if i*(M-j) + j*(N-i) == K:
            flag = True
print('Yes' if flag else 'No')