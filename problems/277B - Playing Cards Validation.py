N = int(input())
fir = ["H","D","C","S"]
sec = ["A","2","3", "4" , "5" , "6" , "7" , "8" , "9" , "T" , "J","Q","K"]
flag = True
cards = []
for i in range(N):
    S = input()
    if S[0] not in fir:
        flag = False
    if S[1] not in sec:
        flag = False
    if S in cards:
        flag = False
    cards.append(S)
print("Yes" if flag else "No")