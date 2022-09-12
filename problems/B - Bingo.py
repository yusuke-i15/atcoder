A = [[0]*3 for i in range(3)]
for i in range(3):
    A[i] = list(map(int,input().split()))
    
N = int(input())

for i in range(N):
    b = int(input())
    for j in range(3):
        for k in range(3):
            if A[j][k] == b:
                A[j][k] = -1

flag = False
for i in range(3):
    if A[i][0] == A[i][1] == A[i][2] == -1:
        flag = True
    if A[0][i] == A[1][i] == A[2][i] == -1:
        flag = True
if A[0][0] == A[1][1] == A[2][2] == -1:
    flag = True
if A[0][2] == A[1][1] == A[2][0] == -1:
    flag = True
print("Yes" if flag else "No")