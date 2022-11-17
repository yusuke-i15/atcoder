S = input()
ans = 0
for i in range(len(S)):
    if S[i] == "U":
        ans += (len(S)-(i+1))
        ans += i*2
    else:
        ans += (len(S)-(i+1))*2
        ans += i
print(ans)