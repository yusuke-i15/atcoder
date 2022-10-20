H = int(input())
ans = 1
while(H>1):
    H = H//2
    ans = 2*ans + 1
print(ans)