S = input()
Q = int(input())
rev = 1
ans = [""]*(4*10**5+5)
l = 2*10**5+2
r = 2*10**5+2+len(S)
ans[l:r] = S
for i in range(Q):
    q = list(input().split())
    if q[0] == "1":
        rev = -rev
    else:
        if q[1] == "1":
            if rev == 1:
                ans[l-1] = q[2] 
                l -= 1
            else:
                ans[r] = q[2]
                r += 1
        else:
            if rev == 1:
                ans[r] = q[2]
                r += 1
            else:
                ans[l-1] = q[2] 
                l -= 1

if rev == -1:
    for i in range(r-1,l,-1):
        print(ans[i],end="")
    print(ans[l])
else:
    for i in range(l,r-1):
        print(ans[i],end="")
    print(ans[r-1])