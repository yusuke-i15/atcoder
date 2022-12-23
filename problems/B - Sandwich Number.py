S = list(input())
flag = True
i = 0
if len(S)%8 == 0:
    for i in range(0,len(S),8):
        if ord(S[i]) < ord("A") or ord(S[i]) > ord("Z"):
            flag = False
        tmp = ""
        for j in range(1,7):    
            if ord(S[i+j]) >= ord("A") and ord(S[i+j]) <= ord("Z"):
                flag = False
            else:
                tmp += S[i+j]
        if int(tmp) < 10**5 or int(tmp) >= 10**6:
            flag = False
        if ord(S[i+7]) < ord("A") or ord(S[i+7]) > ord("Z"):
            flag = False
else:
    flag = False
print('Yes' if flag else 'No')