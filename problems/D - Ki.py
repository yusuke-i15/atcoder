from collections import defaultdict
G = defaultdict(list)
import sys
sys.setrecursionlimit(10**9)
N,Q = map(int,input().split())
G[1].append(-1)
for i in range(N-1):
    u,v = map(int,input().split())
    G[u].append(v)
    G[v].append(u)

def dfs(G,v,p):
    for next_v in G[v]:
        if next_v != p:
            count[next_v] += count[v]
            dfs(G,next_v,v)

count = defaultdict(int)
for i in range(Q):
    v,x = map(int,input().split())
    count[v] += x
dfs(G,1,-1)
for i in range(1,N+1):
    print(count[i],end=" ")