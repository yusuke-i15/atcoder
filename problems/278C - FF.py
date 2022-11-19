from collections import defaultdict
N,Q = map(int,input().split())
dic = defaultdict(int)
for i in range(Q):
    t,a,b = map(int,input().split())
    if t==1:
        if dic[(a,b)] == 0:
            dic[(a,b)] += 1
    if t == 2:
        if dic[(a,b)] == 1:
            dic[(a,b)] -= 1
    if t == 3:
        if dic[(a,b)] == 1 and dic[(b,a)] == 1:
            print("Yes")
        else:
            print("No")