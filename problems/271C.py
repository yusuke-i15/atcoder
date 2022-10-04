from collections import defaultdict
dic_S = defaultdict(int)

N = int(input())
a = list(map(int,input().split()))
for i in a:
    dic_S[i] += 1
set_S = list(set(dic_S))
count = 0
temp = 1
sell = 0
amari = 0
read = 0
sell_n =0
i = set_S[0]
s = 0
for j in range(N):
    if i == temp:
        amari += max(0,dic_S[i]-1)
        temp += 1
        count += 1
        s += 1
        if s < len(set_S):
            i = set_S[s]
    else:
        if sell_n+1 + s <= len(set_S):
            sell_n += 1
            sell_a = set_S[-sell_n] 
            sell += dic_S[sell_a]
            if i == sell_a:
                amari -= dic_S[sell_a]-1
        if sell >= 2:
            temp += 1
            sell -= 2
            count += 1
print(count + (amari+sell)//2)
print(amari,sell)
print((amari+sell)//2)