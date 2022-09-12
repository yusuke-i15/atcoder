S = input()
T = input()

flag = True

if len(S) > len(T):
    flag = False
else:
    for i in range(len(S)):
        if S[i] != T[i]:
            flag = False
print("Yes" if flag else "No")