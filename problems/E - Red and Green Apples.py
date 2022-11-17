X,Y,A,B,C = map(int,input().split())
p = list(map(int,input().split()))
q = list(map(int,input().split()))
r = list(map(int,input().split()))
pqr = []
for i in p:
    pqr.append((i,1))
for i in q:
    pqr.append((i,2))
for i in r:
    pqr.append((i,3))
pqr.sort(reverse=True)
x_c = 0
y_c = 0
r_c = 0
i = 0
tmp = 0
ans = 0
while(tmp < X+Y):
    v,k = pqr[i]
    if k == 3:
        r_c += 1
        ans += v
    if k == 2 and y_c < Y:
        y_c += 1
        ans += v
    if k == 1 and x_c < X:
        x_c += 1
        ans += v
    tmp = x_c + y_c + r_c
    i += 1
print(ans)