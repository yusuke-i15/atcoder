N = int(input())
S = input()

l = -1
for i in range(N):
    if S[i] == "p":
        l = i
        break
if l == -1:
    print(S)
else:
    ans = []
    tmp = ""
    for i in range(l,N):
        if S[i] == "d":
            tmp = "p" + tmp
        else:
            tmp = "d" + tmp
        ans.append(tmp + S[l+len(tmp):])
    ans.sort()
    print(S[:l] + ans[0] + S[l+len(ans[0]):])