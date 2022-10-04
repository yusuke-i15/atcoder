m = int(input())
A = [tuple(map(int,input().split())) for i in range(m)]
n = int(input())
B = [tuple(map(int,input().split())) for i in range(n)]

for i in range(n):
    x = B[i][0] - A[0][0]
    y = B[i][1] - A[0][1]
    for j in range(1,m):
        x_temp = A[j][0] + x
        y_temp = A[j][1] + y
        temp = (x_temp,y_temp)
        if temp in B:
            flag = True
        else:
            flag = False
            break
    if flag:
        print(x,y)
        break