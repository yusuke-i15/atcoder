N = int(input())
S = list(input())
ans = 0
temp = 0
for i in S:
    if i == "I":
        temp += 1
    else:
        temp -= 1
    ans = max(ans,temp)
print(ans)