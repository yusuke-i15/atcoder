from collections import defaultdict
N,M = map(int,input().split())
A = list(map(int,input().split()))
dic = defaultdict(int)
set_d = defaultdict(int)
for i in A:
    dic[i%M] += i
    set_d[i%M] += 1

oku = 0
sets = list(dic.keys())
sets.sort()
seen = defaultdict(int)
for i in sets:
    tmp = 0
    ind = i
    if seen[i] == 0:
        while(set_d[ind] != 0):
            seen[ind] += 1
            tmp += dic[ind]
            ind += 1
            ind = ind%M
            if seen[ind] != 0:
                break
    if i == 0:
        ind = M-1
        if seen[ind] == 0:
            while(set_d[ind] != 0):
                seen[ind] += 1
                tmp += dic[ind]
                ind -= 1
                if seen[ind] != 0:
                    break
    oku = max(oku,tmp)
    seen[i] += 1
print(sum(A)-oku)