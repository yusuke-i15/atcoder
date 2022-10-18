A,B,C = map(int,input().split())
pre = []
a_temp = A
b_temp = B
c_temp = C
ans = 0
while(A%2 == 0 and B%2 == 0 and C%2 == 0):
    A = (b_temp+c_temp)//2
    B = (a_temp+c_temp)//2
    C = (a_temp+b_temp)//2
    a_temp = A
    b_temp = B
    c_temp = C
    ans += 1
    temp = (A,B,C)
    if temp in pre:
        ans = -1
        break
    pre.append(temp)
print(ans)