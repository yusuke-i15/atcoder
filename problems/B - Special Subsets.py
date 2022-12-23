

class UnionFind():
    # 初期化
    def __init__(self, n):
        self.par = [-1] * n
        self.rank = [0] * n
        self.siz = [1] * n

    # 根を求める
    def root(self, x):
        if self.par[x] == -1: return x # x が根の場合は x を返す
        else:
            self.par[x] = self.root(self.par[x]) # 経路圧縮
            return self.par[x]

    # x と y が同じグループに属するか (根が一致するか)
    def issame(self, x, y):
        return self.root(x) == self.root(y)

    # x を含むグループと y を含むグループを併合する
    def unite(self, x, y):
        # x 側と y 側の根を取得する
        rx = self.root(x)
        ry = self.root(y)
        if rx == ry: return False # すでに同じグループのときは何もしない
        # union by rank
        if self.rank[rx] < self.rank[ry]: # ry 側の rank が小さくなるようにする
            rx, ry = ry, rx
        self.par[ry] = rx # ry を rx の子とする
        if self.rank[rx] == self.rank[ry]: # rx 側の rank を調整する
            self.rank[rx] += 1
        self.siz[rx] += self.siz[ry] # rx 側の siz を調整する
        return True
    
    # x を含む根付き木のサイズを求める
    def size(self, x):
        return self.siz[self.root(x)]

#par(x):要素ｘの親頂点の番号（自身が根の場合は-1)
#rank(x):要素ｘの属する根付き木の高さ
#siz(x):要素ｘの属する根付き木に含まれる頂点数
mod = 998244353
N = int(input())
f = list(map(int,input().split()))
UF = UnionFind(N+1)
for i in range(1,N+1):
    UF.unite(i,f[i-1])
sets = set()
for i in range(1,N+1):
    tmp = UF.root(i)
    if tmp == -1:
        sets.add(i)
    else:
        sets.add(tmp)
print(pow(2,len(sets),mod)-1)