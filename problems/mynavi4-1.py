S = input()
for i in S:
    tmp = ord(i)
    if tmp >= 97:
        tmp = tmp - 4
        if tmp < ord("a"):
            tmp = ord("z")+1 - (ord("a")-tmp)
        print(chr(tmp),end="")
    else:
        tmp = tmp - 3
        if tmp < ord("A"):
            tmp = ord("Z")+1 - (ord("A")-tmp)
        print(chr(tmp),end="")
