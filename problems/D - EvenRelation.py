import sys
sys.setrecursionlimit(10**9)
from collections import defaultdict
seen = defaultdict(int)
G = defaultdict(list)
N = int(input())
for i in range(N-1):
    u,v,w = map(int,input().split())
    G[u].append((v,w))
    G[v].append((u,w))
for i in G:
    seen[i] = -1
def dfs(G,v,color):
    seen[v] = color
    for next in G[v]:
        vn = next[0]
        wn = next[1]
        if seen[vn] != -1:
            continue
        if wn%2 == 0:
            dfs(G,vn,color)
        elif color == 0:
            dfs(G,vn,1)
        else:
            dfs(G,vn,0)
dfs(G,1,0)
for i in range(1,N+1):
    print(seen[i])
            