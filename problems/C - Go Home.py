X = int(input())
tmp = 0
ans = 0
for i in range(1,10**5):
    tmp += i
    ans += 1
    if tmp >= X:
        print(ans)
        break