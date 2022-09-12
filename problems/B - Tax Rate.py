N = int(input())
x = int((N//1.08))
x_1 = x + 1
x_2 = x-1
if int(x*1.08) == N:
    print(x)
elif int(x_1*1.08) == N:
    print(x_1)
elif int(x_2*1.08) == N:
    print(x_2)
else:
    print(":(")