N = int(input())
A = list(map(int,input().split()))
flag = True
if N%2 == 1:
    flag = True
else:
    tmp = 0
    for i in A:
        tmp ^= i
    if tmp in A:
        flag = True
    else:
        flag = False
print('Win' if flag else 'Lose')