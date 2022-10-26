N,M = map(int,input().split())
kA = list(map(int,input().split()))
A = kA[1:]
temp = set(A)
for i in range(1,N):
    kA = list(map(int,input().split()))
    A = kA[1:]
    temp = temp&set(A)
print(len(temp))
