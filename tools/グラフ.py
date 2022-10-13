#各ノードに対して隣接するノードをリストとしていれる
from collections import defaultdict
G = defaultdict(list)
E = [(0,1),(0,2),(1,2),(1,3),(2,3)]
for i in E:
    u = i[0]
    v = i[1]
    G[u].append(v)
    G[v].append(u)
print(G)

#重み付き
G = defaultdict(list)
E = [(0,1,5),(0,2,3),(1,2,7),(1,3,9),(2,3,22)]
for i in E:
    u = i[0]
    v = i[1]
    w = i[2]
    G[u].append((v,w))
    G[v].append((u,2))
print(G)