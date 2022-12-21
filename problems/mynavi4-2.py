for i in range(1000,9999):
    for j in range(1000,9999):
        tmp1 = str(i)
        tmp2 = str(j)
        if tmp1[2] == "4" and tmp1[0] == "1" and tmp2[1] == "2" and tmp2[3]=="6":
            one = int(tmp2[3])*i
            if str(one)[1] != "2":
                continue
            two = int(tmp2[2])*i
            if str(two)[0] != "4":
                continue
            four = int(tmp2[0])*i
            if str(four)[3] != "5":
                continue
            ans = i*j
            if str(ans)[0] != "8" or str(ans)[5] != "9":
                continue
            print(i,j)