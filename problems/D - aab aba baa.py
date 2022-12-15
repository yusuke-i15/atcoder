import math
def comb(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

A,B,K = map(int,input().split())
ans = ""
for i in range(A+B):
    if A > 0:
        tmp = comb(A+B-1,B)
        if K > tmp:
            K -= tmp
            ans += "b"
            B -= 1
        else:
            ans += "a"
            A -= 1
    else:
        ans += "b"
        B -= 1
print(ans)