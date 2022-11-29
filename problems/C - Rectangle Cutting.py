W,H,x,y = map(int,input().split())
print(W*H/2,end=" ")
flag = False
if x == W/2 and y == H/2:
    flag = True
print(1 if flag else 0)