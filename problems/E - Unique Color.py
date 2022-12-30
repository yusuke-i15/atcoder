from collections import defaultdict
import sys
sys.setrecursionlimit(10**9)
N = int(input())
C = list(map(int,input().split()))
G = defaultdict(list)
#無向グラフ
for i in range(N-1):
    u,v = map(int,input().split())
    G[u].append(v)
    G[v].append(u)
colors = defaultdict(int)

def dfs(G,v,p,ans):
    if colors[C[v-1]] == 0:
        ans.append(v)
    colors[C[v-1]] += 1
    for next_v in G[v]:
        if next_v != p:
            dfs(G,next_v,v,ans)
    colors[C[v-1]] -= 1
root = 1 #根に
ans = []
dfs(G,root,-1,ans)
ans.sort()
for i in ans:
    print(i)