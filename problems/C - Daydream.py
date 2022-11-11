S = input()
S = "".join(reversed(S))
i = 0
flag = True
while(i < len(S)):
    if S[i:i+5] == "maerd":
        i += 5
    elif S[i:i+7] == "remaerd":
        i += 7
    elif S[i:i+5] == "esare":
        i += 5
    elif S[i:i+6] == "resare":
        i += 6
    else:
        flag = False
        break
print("YES" if flag else "NO")