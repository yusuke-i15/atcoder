T = int(input())
for i in range(T):
    a,s = map(int,input().split())
    dif = s - 2*a
    if dif >= 0 and dif&a == 0:
        print("Yes")
    else:
        print("No")