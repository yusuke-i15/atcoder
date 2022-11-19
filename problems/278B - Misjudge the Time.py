H,M = map(int,input().split())
A = H//10
B = H%10
C = M//10
D = M%10
while(True):
    tmp_h = A*10+C
    tmp_m = B*10+D
    if tmp_h >= 0 and tmp_h <=23 and tmp_m <=59 and tmp_m >=0:
        print(A*10+B,C*10+D)
        break
    D += 1
    if D >= 10:
        D = 0
        C += 1
    if C >= 6:
        B += 1
        C = 0
    if B >= 10:
        A += 1
        B = 0
    if A*10+B>=24:
        A = 0
        B = 0