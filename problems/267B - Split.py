S =input()

if S[0] == "1":
    print("No")
else:
    temp = [0]*7
    if S[6] == "1":
        temp[0] = 1
    if S[3] == "1":
        temp[1] = 1
    if S[1] == "1" or S[7] == "1":
        temp[2] = 1
    if S[4] == "1":
        temp[3] = 1
    if S[8] == "1" or S[2] == "1":
        temp[4] = 1
    if S[5] == "1":
        temp[5] = 1
    if S[9] == "1":
        temp[6] = 1
    left = False
    mid = False
    right = False
    for i in range(7):
        if temp[i] == 1:
            left = True
        elif left == True and temp[i] == 0:
            mid = True
        if left == True and mid == True and temp[i] == 1:
            print("Yes")
            right = True
            break
    if right != True:
        print("No")