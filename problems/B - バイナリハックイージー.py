s = list(input())
ans = ""
for i in s:
    if i == "B" and ans != "":
        ans = ans[:-1]
    elif i != "B":
        ans += i
print(ans)