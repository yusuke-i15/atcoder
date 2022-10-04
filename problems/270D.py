N,K = map(int,input().split())
N2 = N
A = list(map(int,input().split()))

A = sorted(A,reverse=True)
turn = 1
count = 0
while(N > 0):
    for i in range(len(A)):
        if A[i] <= N:
            temp = A[i]
            break
    N = N-temp
    if turn == 1:
        count += temp
    turn = turn*(-1)

N2 = N2 - A[1]
count2 = A[1]
turn = -1
while(N2 > 0):
    for i in range(len(A)):
        if A[i] <= N2:
            temp = A[i]
            break
    N2 = N2-temp
    if turn == 1:
        count2 += temp
    turn = turn*(-1)


if count >= count2:
    print(count)
else:
    print(count2)
