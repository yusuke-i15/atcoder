from collections import defaultdict
S = input()
dic = defaultdict(int)
for i in S:
    dic[i] += 1
if abs(dic["a"] -dic["b"]) <= 1 and abs(dic["c"] -dic["b"]) <= 1 and abs(dic["a"] -dic["c"]) <= 1:
    print("YES")
else:
    print("NO")