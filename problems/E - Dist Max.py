N = int(input())
xpy = []
ymx = []
for i in range(N):
    x,y = map(int,input().split())
    xpy.append(x+y)
    ymx.append(y-x)
xpy.sort()
ymx.sort()
print(max(xpy[-1]-xpy[0],ymx[-1]-ymx[0]))