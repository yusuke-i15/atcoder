N = int(input())
ans = ""
if N == 0:
    ans = "0"
while N != 0:
    tmp = N%2
    ans = str(tmp) + ans
    N -= tmp
    N = N//(-2)
print(ans)