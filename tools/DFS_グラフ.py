import sys
sys.setrecursionlimit(10**9)
from collections import defaultdict
G = defaultdict(list)
E = [(0,1),(0,2),(1,3),(2,3)]
#無向グラフ
for i in E:
    u = i[0]
    v = i[1]
    G[u].append(v)
    G[v].append(u)
print(G)

seen = defaultdict(int)

first_order = []
last_order = []

def dfs(G,v,order):
    order += 1
    seen[v] = order
    first_order.append(v)
    for next_v in G[v]:
        if seen[next_v] == 0:
            dfs(G,next_v,order)
    last_order.append(v)
order = 0
dfs(G,0,order)
print(first_order)
print(last_order)
print(seen)