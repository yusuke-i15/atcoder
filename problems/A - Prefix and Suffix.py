N = int(input())
s = input()
t = input()

flag2 = True
for i in range(N):
    flag = True
    for j in range(N-i):
        if s[i+j] != t[j]:
            flag = False
    if flag:
        flag2 = False
        print(N+i)
        break
if flag2:
    print(N*2)