s = input()
ans = 0
bc = [0]*len(s)
for i in range(len(s)-1,-1,-1):
    if s[i] == "C" and i-1 >= 0 and s[i-1] == "B":
        if i-2 >= 0:
            bc[i-2] = bc[i] + 1
    if s[i] == "A":
        if i-1>= 0:
            bc[i-1] = bc[i]
for i in range(len(s)-1,-1,-1):
    if s[i] == "A":
        if i + 1 < len(s) and s[i+1] == "A":
            bc[i] = bc[i+1]
for i in range(len(s)):
    if s[i] == "A":
        ans += bc[i]
print(ans)