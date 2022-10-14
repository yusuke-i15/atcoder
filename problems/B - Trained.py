N = int(input())
a = [0]*N
for i in range(N):
    a[i] = int(input())
temp = a[0]
count = 1
flag = False
for i in range(N):
    if temp == 2:
        flag = True
        break
    temp = a[temp-1]
    count += 1
print(count if flag else -1)