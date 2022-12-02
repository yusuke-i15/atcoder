from collections import defaultdict
K = int(input())
ans = -1
cnt = 1
tmp = 7
dic = defaultdict(int)
while(True):
    tmp = tmp%K
    dic[tmp] += 1
    if dic[0] == 1:
        ans = cnt 
        break
    if dic[tmp] >= 2:
        break
    cnt += 1
    tmp = 10*tmp + 7

print(ans)