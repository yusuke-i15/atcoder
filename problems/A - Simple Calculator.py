x,y = map(int,input().split())
ans = 0
if x>y:
    ans += 1
    if abs(x)>abs(y):
        x = -x
    else:
        y = -y
if x<=y:
    if x*y >= 0:
        print(y-x + ans)
    else:
        print(min(y-x,1+abs(-y-x)) + ans)