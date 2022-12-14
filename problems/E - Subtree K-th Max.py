from collections import defaultdict
import sys
sys.setrecursionlimit(10**9)

N,Q = map(int,input().split())
X = list(map(int,input().split()))
G = defaultdict(list)
#無向グラフ
for i in range(N-1):
    u,v = map(int,input().split())
    G[u].append(v)
    G[v].append(u)
Xs = defaultdict(list)

def dfs(G,v,p,d):
    Xs[v].append(X[v-1])
    for next_v in G[v]:
        if next_v != p:
            dfs(G,next_v,v,d+1)
    for c in G[v]:
        if c != p:
            for x in Xs[c]:
                Xs[v].append(x)
    Xs[v].sort(reverse=True)
    if len(Xs[v])>20:
        Xs[v] = Xs[v][:20]
root = 1 #仮に頂点0を根に
dfs(G,root,-1,0)

for i in range(Q):
    v,k = map(int,input().split())
    print(Xs[v][k-1])