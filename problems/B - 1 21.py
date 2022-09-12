a,b = input().split()
s = a + b
s = int(s)
temp = int(s ** 0.5)
if temp*temp == s:
    print("Yes")
else:
    print("No")
