N = int(input())
a = list(map(int,input().split()))
two = 0
four = 0
ki = 0
for i in a:
    if i%4 == 0:
        four += 1
    elif i%2 == 0:
        two += 1
    else:
        ki += 1
if two >= 2:
    if ki > four:
        print("No")
    else:
        print("Yes")
else:
    if two + ki - 1 <= four:
        print("Yes")
    else:
        print("No")
