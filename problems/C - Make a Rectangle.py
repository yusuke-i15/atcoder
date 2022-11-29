from collections import defaultdict
N = int(input())
A = list(map(int,input().split()))
dic = defaultdict(int)
for i in A:
    dic[i] += 1
l = [0,0]
for i in dic:
    if dic[i] >= 4:
        l.append(i)
        l.append(i)
    elif dic[i] >= 2:
        l.append(i)
l.sort(reverse=True)
print(l[0]*l[1])    