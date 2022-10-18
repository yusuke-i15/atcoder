from collections import defaultdict
s = int(input())
dic = defaultdict(int)
dic[s] += 1
for i in range(1,10**6+10):
    if s%2 == 0:
        s = s/2
    else:
        s = 3*s + 1
    if dic[s] >= 1:
        print(i+1)
        break
    else:
        dic[s] += 1