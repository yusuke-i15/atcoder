from collections import defaultdict
N = int(input())
S = [input() for i in range(N)]
dic = defaultdict(int)
ans = 0
for i in S:
    ans += i.count("AB")
    if i[0] == "B" and i[-1] == "A":
        dic["AB"] += 1
    elif i[0] == "B":
        dic["B"] += 1
    elif i[-1] == "A":
        dic["A"] += 1
if dic["AB"] >= 1:
    if dic["A"] > 0 or dic["B"] > 0:
        print(ans+max(0,dic["AB"]-1)+min(dic["A"]+1,dic["B"]+1))
    else:
        print(ans+max(0,dic["AB"]-1))
else:
    print(ans+min(dic["A"],dic["B"]))