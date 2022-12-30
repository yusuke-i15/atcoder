S = input()
i = 0
ans = len(S)
while(i<len(S)-1):
    if S[i] == "0" and S[i+1] == "0":
        ans -= 1
        i += 1
    i += 1
print(ans)