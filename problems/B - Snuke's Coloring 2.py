W,H,N = map(int,input().split())
lx = 0
rx = W
uy = H
dy = 0
for i in range(N):
    x,y,a = map(int,input().split())
    if a == 1:
        lx = max(lx,x)
    elif a == 2:
        rx = min(rx,x)
    elif a == 3:
        dy = max(dy,y)
    else:
        uy = min(uy,y)
print(max(0,(rx-lx))*max(0,(uy-dy)))