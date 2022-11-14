from collections import defaultdict
N = int(input())
A = list(map(int,input().split()))
MOD = 10**9+7
dic = defaultdict(lambda: -1)
if N%2 == 0:
    for i in range(1,N,2):
        dic[i] = 0
else:
    for i in range(0,N,2):
        dic[i] = 0
flag = True
for i in A:
    if dic[i] == -1:
        flag = False
    else:
        dic[i] += 1
    if dic[i] > 2:
        flag = False
    if i == 0 and dic[i] >= 2:
        flag = False
if flag:
    print(pow(2,N//2,MOD))
else:
    print(0)