from collections import deque
from collections import defaultdict
S = input()
flag = True
dic = defaultdict(deque)
box = defaultdict(int)
cnt = 0
for i in S:
    if ord(i) >= ord("a") and ord(i) <= ord("z"):
        if box[i] >= 1:
            flag = False
            break
        box[i] += 1
        dic[cnt].append(i)
    if i == "(":
        cnt += 1
    if i == ")":
        for j in range(len(dic[cnt])):
            box[dic[cnt].pop()] -= 1
        cnt -= 1
print('Yes' if flag else 'No')