A,B,C,X,Y = map(int,input().split())

if (A+B)//2 < C:
    print(A*X+B*Y)
else:
    result = A*X+B*Y
    if X > Y:
        for i in range(X+1):
            temp = i*2*C + (X-i)*A + max(0,(Y-i)*B)
            result = min(result,temp)
    else:
        for i in range(Y+1):
            temp = i*2*C + max(0,(X-i)*A) + (Y-i)*B
            result = min(result,temp)
    print(result)