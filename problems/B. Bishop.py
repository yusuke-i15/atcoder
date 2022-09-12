H, W = map(int,input().split())

if H==1 or W == 1:
    print(1)
elif H%2 == 0 or W%2 == 0:
    print(W*H//2)
else:
    print((W*H+1)//2)