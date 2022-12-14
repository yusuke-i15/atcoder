import sys
sys.setrecursionlimit(10**9)
from collections import defaultdict

N = int(input())
G = defaultdict(list)
#無向グラフ
for i in range(N-1):
    u,v = map(int,input().split())
    G[u].append(v)
    G[v].append(u)

seen = defaultdict(int)
first_order = []
last_order = []
ansl = defaultdict(int)
ansr = defaultdict(int)

def dfs(G,v):
    seen[v] = 1
    if len(G[v]) == 1 and v != 1:
        ansl[v] = 1
        ansr[v] = 1
    for next_v in G[v]:
        if seen[next_v] == 0:
            dfs(G,next_v)


depth = defaultdict(int)
subtree_size = defaultdict(int)
def dfs2(G,v,p,d):
    depth[v] = d
    for next_v in G[v]:
        if next_v != p:
            dfs2(G,next_v,v,d+1)
    if len(G[v]) >= 2 or v == 1:
        tmpmin = float("inf")
        tmpmax = -float("inf")
        for c in G[v]:
            if c != p:
                tmpmin = min(tmpmin,ansl[c])
                tmpmax = max(tmpmax,ansr[c])
        ansl[v] = tmpmin
        ansr[v] = tmpmax
dfs(G,1)
tmp = 1
for i in ansl:
    ansl[i] = tmp
    ansr[i] = tmp
    tmp += 1
root = 1 #仮に頂点0を根に
dfs2(G,root,-1,0)
for i in range(1,N+1):
    print(ansl[i],ansr[i])