S = int(input())
X1 = 0
Y1 = 0
Y2 = 1
X2 = 10**9
Y3 = S//X2 + 1
if Y3 > 10**9:
    Y3 -= 1
    X3 = 0
else:
    X3 = 10**9 - S%X2
print(X1,Y1,X2,Y2,X3,Y3)