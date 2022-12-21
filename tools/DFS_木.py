#再帰だがらpythonの方がいいかも
from collections import defaultdict
import sys
sys.setrecursionlimit(10**9)
G = defaultdict(list)
E = [(0,1),(0,2),(1,3),(1,4)]
#無向グラフ
for i in E:
    u = i[0]
    v = i[1]
    G[u].append(v)
    G[v].append(u)
print(G)
depth = defaultdict(int)
subtree_size = defaultdict(int)

def dfs(G,v,p,d):
    depth[v] = d
    for next_v in G[v]:
        if next_v != p:
            dfs(G,next_v,v,d+1)
    subtree_size[v] = 1
    for c in G[v]:
        if c != p:
            subtree_size[v] += subtree_size[c]
root = 0 #仮に頂点0を根に
dfs(G,root,-1,0)
print(depth)
print(subtree_size)