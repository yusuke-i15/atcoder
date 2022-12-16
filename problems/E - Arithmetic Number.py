X = input()
if len(X)>10:
    tmp = X[0]
    if int(tmp*len(X)) >= int(X):
        ans = tmp*len(X)
    else:
        tmp = int(tmp) + 1
        ans = str(tmp)*len(X)
elif len(X) <= 2:
    ans = X
elif len(X) >= 6:
    if len(X) != 10:
        ansA = [int(X[0]*len(X))]
        tmp = ""
        for i in range(1,len(X)+1):
            tmp += str(i)
        ansA.append(int(tmp))
        tmp = ""
        for i in range(len(X)-1,-1,-1):
            tmp += str(i)
        ansA.append(int(tmp))
        for i in range(int(X[0]),len(X)):
            ansA.append(int(str(i)*len(X)))
    else:
        ansA = [int(X[0]*len(X))]
        tmp = ""
        for i in range(len(X)-1,-1,-1):
            tmp += str(i)
        ansA.append(int(tmp))
        for i in range(int(X[0]),len(X)):
            ansA.append(int(str(i)*len(X)))
    ansA.sort()
    for i in ansA:
        if int(X) <= i:
            ans = i
            break
else:
    while(True):
        flag = True
        tmp = int(X[1]) - int(X[0])
        for i in range(1,len(X)-1):
            if int(X[i+1]) - int(X[i]) != tmp:
                flag = False
                break
        if flag:
            ans = X
            break
        X = int(X)+1
        X = str(X)
print(ans)