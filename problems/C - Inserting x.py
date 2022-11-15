s = input()
ans = 0
l = 0
r = len(s)-1
while(True):
    if l >= r:
        break
    if s[l] == s[r]:
        l += 1
        r -= 1
    else:
        if s[l] == "x":
            ans += 1
            l += 1
        elif s[r] == "x":
            ans += 1
            r -= 1
        else:
            ans = -1
            break
print(ans)
        