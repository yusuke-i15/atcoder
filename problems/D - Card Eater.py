from collections import defaultdict
N = int(input())
A = list(map(int,input().split()))
dic = defaultdict(int)
for i in A:
    dic[i] += 1
tmp = 0
for i in dic:
    if dic[i] >= 2:
        tmp += dic[i]-1
if tmp%2 == 0:
    print(len(dic))
else:
    print(len(dic)-1)