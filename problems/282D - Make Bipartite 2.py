import sys
sys.setrecursionlimit(10**9)
from collections import defaultdict
N,M = map(int,input().split())
G = defaultdict(list)
for i in range(M):
    u,v = map(int,input().split())
    u -= 1
    v -= 1
    G[u].append(v)
    G[v].append(u)

# 頂点 v を始点とした深さ優先探索
def dfs(v, G, color,a):
    if color[v] == 0:
        dic_b[a] += 1
    else:
        dic[a].append(v)
    # G[v] に含まれる頂点 v2 について、
    for v2 in G[v]:
        # v2 がすでに探索済みならば、スキップする
        if color[v2] != -1:
            # 隣り合う頂点どうしが同じ色なら、答えは No
            if color[v2] == color[v]: return False
            continue
        # そうでなければ、頂点 v2 の色を color[v] と逆にしたうえで
        # v2 始点で深さ優先探索を行う (関数を再帰させる)
        color[v2] = 1 - color[v]
        if not dfs(v2, G, color,a): return False
    return True
color = [-1 for _ in range(N)]
flag = True
ans = 0
# 全ての頂点について
dic = defaultdict(list)
dic_b = defaultdict(int)
tmp = 0
for v in range(N):
    # 頂点 v がすでに訪問済みであれば、スキップ
    if color[v] != -1: continue
    # そうでなければ、頂点 v を含む連結成分は未探索
    # 頂点 v の色を白で決め打ちしたうえで、深さ優先探索を行う
    color[v] = 1
    if not dfs(v, G, color,v):
        flag = False
    else:
        dicb = dic_b[v]
        ans += dicb*len(dic[v])
        if tmp == 0:
            tmp = len(dic[v])+dicb
        else:
            ans += tmp*(len(dic[v])+dicb)
            tmp += len(dic[v])+dicb
    if flag == False:
        break
if flag:
    print(ans - M)
else:
    print(0)