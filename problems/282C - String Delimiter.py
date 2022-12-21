N = int(input())
S = list(input())
flag = 1
for i in range(N):
    if S[i] == '"':
        flag *= -1
    if flag == 1 and S[i] == ",":
        S[i] = "."
print("".join(S))