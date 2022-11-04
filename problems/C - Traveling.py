N = int(input())
t = 0
x = 0
y = 0
flag = True
for i in range(N):
    ti,xi,yi = map(int,input().split())
    x_dif = abs(xi-x)
    y_dif = abs(yi-y)
    t_dif = ti-t
    if x_dif+y_dif > t_dif:
        flag = False
    if (t_dif-(x_dif+y_dif))%2 != 0:
        flag = False
    x = xi
    y = yi
    t = ti
print("Yes" if flag else "No")