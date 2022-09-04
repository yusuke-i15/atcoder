N,A,B = map(int,input().split())
S = input()

A_n = 0
B_n = 0
for i in range(N):
    if S[i] == "a" and A_n+B_n < A+B:
        A_n += 1
        print("Yes")
    elif S[i] == "b" and B_n < B and A_n+B_n < A+B:
        B_n += 1
        print("Yes")
    else:
        print("No")