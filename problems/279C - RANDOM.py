from collections import defaultdict
H,W = map(int,input().split())
S = [input() for i in range(H)]
T = [input() for i in range(H)]
dic = defaultdict(int)
for i in range(W):
    tmp = ""
    for j in range(H):
        tmp += S[j][i]
    dic[tmp] += 1
flag = True
for i in range(W):
    tmp = ""
    for j in range(H):
        tmp += T[j][i]
    if dic[tmp] == 0:
        flag = False
    else:
        dic[tmp] -= 1
print("Yes" if flag else "No")