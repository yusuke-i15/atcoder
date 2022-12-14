from collections import defaultdict
N = int(input())
s = list(input())

dic = defaultdict(list)
for i in range(N):
    dic[s[i]].append(i)
r = N
dic = dict(sorted(dic.items(),key = lambda x:x[0]))
for i in range(N):
    if i >= r:
        break
    for j in dic:
        if j >= s[i]:
            break
        while( len(dic[j]) > 0 and dic[j][-1] > r):
            dic[j].pop()
        if len(dic[j]) > 0 and i < dic[j][-1] and i <= r:
            r = dic[j].pop()
            s[i],s[r] = s[r],s[i]
            r = r - 1
            break
print("".join(s))