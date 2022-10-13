#二次元配列
#pythonだとTLE pypyだとMLEなった
M,N = map(int,input().split())
K = int(input())
T = [list(input()) for i in range(M)]
 
Js = [[0]*(N+1) for i in range(M+1)]
 
for i in range(M):
    for j in range(N):
        Js[i+1][j+1] = Js[i][j+1] + Js[i+1][j] - Js[i][j]
        if T[i][j] == "J":
            Js[i+1][j+1] += 1
        if T[i][j] == "O":
            Js[i+1][j+1] += 10**5
 
 
for k in range(K):
    a,b,c,d = map(int,input().split())
    temp = Js[c][d] - Js[a-1][d] - Js[c][b-1] + Js[a-1][b-1]
    ans1 = temp%(10**5)
    print(ans1,end=" ")
    ans2 = temp//(10**5)
    print(ans2,end=" ")
    print((c-a+1)*(d-b+1) - ans1 - ans2)


#numpy_バージョン
"""
import numpy as np

M,N = map(int,input().split())
K = int(input())
T = [input() for i in range(M)]

Js = np.zeros((M+1,N+1))

for i in range(M):
    for j in range(N):
        if T[i][j] == "J":
            Js[i+1][j+1] += 1
        if T[i][j] == "O":
            Js[i+1][j+1] += 10**5

Js = Js.cumsum(axis=0).cumsum(axis=1)

for k in range(K):
    a,b,c,d = map(int,input().split())
    temp = Js[c][d] - Js[a-1][d] - Js[c][b-1] + Js[a-1][b-1]
    ans1 = int(temp%(10**5))
    print(ans1,end=" ")
    ans2 = int(temp//(10**5))
    print(ans2,end=" ")
    print((c-a+1)*(d-b+1) - ans1 - ans2)
"""

    

#模範解答
"""
import numpy as np
import sys

read = sys.stdin.buffer.read
input = sys.stdin.buffer.readline
m, n = map(int, input().split())
q = int(input())

field = np.zeros((m + 1, n + 1), 'S1')
for i in range(1, m + 1):
    field[i, 1:] = np.frombuffer(input().rstrip(), 'S1')

Q = np.array(read().split(), np.int16)

J = (field == b'J').cumsum(axis=0).cumsum(axis=1)
O = (field == b'O').cumsum(axis=0).cumsum(axis=1)
I = (field == b'I').cumsum(axis=0).cumsum(axis=1)
A, B, C, D = Q[0::4] - 1, Q[1::4] - 1, Q[2::4], Q[3::4]
J = J[C, D] - J[A, D] - J[C, B] + J[A, B]
O = O[C, D] - O[A, D] - O[C, B] + O[A, B]
I = I[C, D] - I[A, D] - I[C, B] + I[A, B]

print('\n'.join("{} {} {}".format(j, o, i) for j, o, i in zip(J, O, I)))
"""