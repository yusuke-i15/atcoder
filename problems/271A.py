N = int(input())

a = N//16
b = N%16

if a == 10:
    print("A",end="")
elif a == 11:
    print("B",end="")
elif a == 12:
    print("C",end="")
elif a == 13:
    print("D",end="")
elif a == 14:
    print("E",end="")
elif a == 15:
    print("F",end="")
else:
    print(a,end="")
a = b
if a == 10:
    print("A",end="")
elif a == 11:
    print("B",end="")
elif a == 12:
    print("C",end="")
elif a == 13:
    print("D",end="")
elif a == 14:
    print("E",end="")
elif a == 15:
    print("F",end="")
else:
    print(a,end="")