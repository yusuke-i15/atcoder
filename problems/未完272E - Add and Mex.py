N,M = map(int,input().split())
A = list(map(int,input().split()))
b = [0]*N
for i in range(1,1+N):
    temp = 0
    while(A[i-1]+temp*i < 0):
        temp += 1
    b[i-1] = temp
A = A[b.so()]
print(A)
