N,X = map(int,input().split())
a = [1]
p = [1]
for i in range(N):
    a.append(a[-1]*2+3)
    p.append(p[-1]*2+1)
def f(level,x):
    if x == 0:
        return 0
    if level == 0:
        return 1
    if x == 1:
        return 0
    x = x - 1 
    if x > a[level-1]:
        return p[level-1] + 1 + f(level-1,x-a[level-1]-1)
    else:
        return f(level-1,x)
print(f(N,X))