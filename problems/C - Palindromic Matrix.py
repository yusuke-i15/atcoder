from collections import defaultdict
H,W = map(int,input().split())
a = [input() for i in range(H)]
dic = defaultdict(int)
for i in range(H):
    for j in range(W):
        dic[a[i][j]] += 1

flag = True
amari2 = 0
amari1 = 0
for i in dic:
    tmp = dic[i]%4
    if tmp == 2:
        amari2 += 1
    elif tmp == 1:
        amari1 += 1
    elif tmp == 3:
        amari2 += 1
        amari1 += 1
if H%2 == 1 and W%2 == 1:
    amari1 -=1
if H%2 == 1:
    amari2 = amari2 - max(0,W//2)
if W%2 == 1:
    amari2 = amari2 - max(0,H//2)
if amari2 <= 0 and amari1 <= 0:
    print("Yes")
else:
    print("No")
