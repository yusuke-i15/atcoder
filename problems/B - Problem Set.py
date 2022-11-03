from collections import defaultdict
N = int(input())
D = list(map(int,input().split()))
M = int(input())
T = list(map(int,input().split()))
dic_D = defaultdict(int)
dic_T = defaultdict(int)
for i in D:
    dic_D[i] += 1
for i in T:
    dic_T[i] += 1
flag = True
for i in dic_T:
    if dic_T[i] > dic_D[i]:
        flag = False
print("YES" if flag else "NO")