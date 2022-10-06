#各ノードに対して隣接するノードをリストとしていれる
from collections import defaultdict
dic_S = defaultdict(list)
E = [(0,1),(0,2),(1,2),(1,3),(2,3)]
for i in E:
    u = i[0]
    v = i[1]
    dic_S[u].append(v)
    dic_S[v].append(u)
print(dic_S)

#重み付き
dic_S = defaultdict(list)
E = [(0,1,5),(0,2,3),(1,2,7),(1,3,9),(2,3,22)]
for i in E:
    u = i[0]
    v = i[1]
    w = i[2]
    dic_S[u].append((v,w))
    dic_S[v].append((u,2))
print(dic_S)