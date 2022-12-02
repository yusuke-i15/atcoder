from collections import defaultdict
N,C = map(int,input().split())
dic = defaultdict(int)
sets = set()
for i in range(N):
    a,b,c = map(int,input().split())
    dic[a] += c
    dic[b+1] -= c
    sets.add(a)
    sets.add(b+1)
ans = 0
sets = sorted(list(sets))

for i in range(len(sets)-1):
    day = sets[i+1] - sets[i]
    if dic[sets[i]] > C:
        ans += C*day
    else:
        ans += dic[sets[i]]*day
    dic[sets[i+1]] += dic[sets[i]]    
print(ans)