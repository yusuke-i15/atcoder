from collections import defaultdict
from collections import deque
N = int(input())
dic = defaultdict(list)
sets = []
dic_s = defaultdict(int)
for i in range(N):
    s = input()
    dic[s[0]].append(s[-1])
    dic_s[(s[0],s[-1])] += 1
    sets.append((s[0],s[-1]))
sets = list(set(sets))
flag = False
for s,n in sets:
    #dist:開始点からの距離_今回はノード0
    dist = defaultdict(lambda: -1)
    dist[s] = 0
    q = deque()
    qn = deque()
    q.append(s)
    count = defaultdict(int)
    count[(s,n)] += 1
    while(len(q) > 0):
        v = q.popleft()
        for next_v in dic[v]:
            if count[(v,next_v)] >= dic_s[(v,next_v)]:
                continue
            qn.append(next_v)
            dist[next_v] = dist[v] + 1
    for i in range(len(qn))
    print(dist)