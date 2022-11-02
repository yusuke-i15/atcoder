import numpy as np
H,W = map(int,input().split())
s = [input() for i in range(H)]

A = np.zeros((H,W))
for j in range(W):
    temp = 0
    for i in range(H):
        if s[i][j] != "#":
            temp += 1
            A[i][j] = temp
        else:
            temp = 0
ans = 0
for i in range(H):
    for j in range(W):
        temp = A[i][j]
        right = j
        left = j
        for k in range(j,W):
            if A[i][k] >= temp:
                right += 1
            else:
                break
        for k in range(1,j+1):
            if A[i][j-k] >= temp:
                left -=1
            else:
                break
        ans = max(ans,(right-left)*temp)

print(int(ans))