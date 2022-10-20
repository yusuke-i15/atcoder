from collections import defaultdict
S = list(input())
dic = defaultdict(int)
flag = True
for i in S:
    dic[i] += 1
    if dic[i] >= 2:
        flag = False
        break
print("yes" if flag else "no")