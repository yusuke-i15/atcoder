N = int(input())
def f(a,b):
    return a**3 + a**2*b + a*b**2 + b**3
j = 10**6
ans = float("inf")
for i in range(10**6+1):
    while(f(i,j)>=N and j >= 0):
        ans = min(ans,f(i,j))
        j -= 1
print(ans)