X,Y,Z = map(int,input().split())

if X*Y < 0 or abs(X) < abs(Y):
    print(abs(X))
elif Y*Z > 0 and abs(Y) < abs(Z):
    print(-1)
elif X*Z > 0:
    print(abs(X))
else:
    print(2*abs(Z)+abs(X))
