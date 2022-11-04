A,B,C = map(int,input().split())
flag = False
for i in range(10**5):
    if (B*i+C)%A == 0:
        flag = True
        break
print("YES" if flag else "NO")