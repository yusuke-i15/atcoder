A,B = map(int,input().split())
S = list(input())
flag = True
for i in range(A):
    if S[i] == "-":
        flag = False
if S[A] != "-":
    flag = False
for i in range(A+1,A+B+1):
    if S[i] == "-":
        flag = False
print("Yes" if flag else "No")