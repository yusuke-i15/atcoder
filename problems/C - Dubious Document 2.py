S = input()
T = input()

ans = []
for i in range(len(S)):
    temp = list(S)
    for j in range(len(T)):
        if i + j > len(S)-1:
            flag = False
        else:
            if S[i+j] == T[j]:
                flag = True
            elif S[i+j] == "?":
                flag = True
                temp[i+j] = T[j]
            else:
                flag = False
                break
    if flag:
        temp = [i.replace("?","a") for i in temp]
        ans.append(temp)
if ans == []:
    print("UNRESTORABLE")
else:
    ans.sort()
    print(*ans[0],sep="")