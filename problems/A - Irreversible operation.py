S = list(input())

ans = 0
count = 0
for i in S:
    if i == "B":
        count += 1
    elif i == "W":
        ans += count
print(ans)