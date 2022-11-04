c = [list(map(int,input().split())) for i in range(3)]

flag = False
for a1 in range(101):
    b1 = c[0][0] - a1
    b2 = c[0][1] - a1
    b3 = c[0][2] - a1
    a2 = c[1][0] - b1
    a3 = c[2][0] - b1
    if a2+b2 == c[1][1] and a2+b3 == c[1][2] and a3+b2==c[2][1] and a3+b3 == c[2][2]:
        flag = True
print("Yes" if flag else "No")