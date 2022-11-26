A,B = map(int,input().split())
g = int((A/(2*B))**(2/3))
ans = float("inf")
if g+ 1 != 0:
    ans = min(ans,A/((g+1)**0.5)+B*g)
if g != 0:
    ans = min(ans,A/(g**0.5)+B*(g-1))
if g+2 != 0:
    ans = min(ans,A/((g+2)**0.5)+B*g+B)
print(ans)