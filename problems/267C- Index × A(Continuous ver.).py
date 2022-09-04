N,M = map(int,input().split())
A = list(map(int,input().split()))

rui = [0]*(N+1)
rui[1]  = A[0]
for i in range(1,N):
    rui[i+1] = rui[i]+A[i]

temp = 0
temp_j = 1
for i in range(M):
    temp += A[i]*temp_j
    temp_j += 1

max_v = temp
for i in range(1,N-(M-1)):
    temp = temp + A[i-1+M]*M -(rui[M+i-1]-rui[i-1])
    if temp > max_v:
        max_v = temp

print(max_v)