w = input()
temp = list(set(w))
flag = True
for i in temp:
    if w.count(i)%2 != 0:
        flag = False
        break
print("Yes" if flag else "No")