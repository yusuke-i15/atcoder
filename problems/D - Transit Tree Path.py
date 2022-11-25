from collections import defaultdict
import sys
sys.setrecursionlimit(10**9)

G = defaultdict(list)
N = int(input())
G = defaultdict(list)
for i in range(N-1):
    a,b,c = map(int,input().split())
    G[a].append((b,c))
    G[b].append((a,c))
Q,K = map(int,input().split())
depth = defaultdict(int)
dis = defaultdict(int)
def dfs(G,v,p,d):
    dis[v] = d
    for next_v,c in G[v]:
        if next_v != p:
            dis[next_v] = d+c
            dfs(G,next_v,v,d+c)
root = K #仮に頂点0を根に
dfs(G,root,-1,0)
for i in range(Q):
    x,y = map(int,input().split())
    print(dis[x]+dis[y])