import sys
sys.setrecursionlimit(10**9)
from collections import defaultdict
from collections import deque

N,X,Y = map(int,input().split())
G = defaultdict(list)
#無向グラフ
for i in range(N-1):
    u,v = map(int,input().split())
    G[u].append(v)
    G[v].append(u)

seen = defaultdict(int)
first_order = deque()
def dfs(G,v,order):
    order += 1
    seen[v] = order
    first_order.append(v)
    if v == Y:
        print(*first_order)
    for next_v in G[v]:
        if seen[next_v] == 0:
            dfs(G,next_v,order)
    first_order.pop()
order = 0
dfs(G,X,order)