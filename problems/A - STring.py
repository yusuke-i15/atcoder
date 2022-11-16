X = input()
tmp = 0
ans = len(X)
for i in X:
    if i == "S":
        tmp += 1
    if i == "T" and tmp > 0:
        tmp -= 1
        ans -= 2
print(ans)