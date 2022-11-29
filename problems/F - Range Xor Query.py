"""
区間[x,y)に対する操作O(log n)
区間上の値の更新、
任意の区間上の最小値や合計値を取得できる
PyPy3にした方がいいかも
"""
class SegTree:
    def __init__(self, op, e, n, v=None):
        self._n = n#要素数
        self._op = op#演算
        self._e = e#単位元
        self._log = (n - 1).bit_length()# 2^(_log) >= n となる最小の整数
        self._size = 1 << self._log# 木の深さ
        self._d = [self._e()] * (self._size << 1)#全体の大きさ
        if v is not None:
            for i in range(self._n):
                self._d[self._size + i] = v[i]
            for i in range(self._size - 1, 0, -1):
                self._d[i] = self._op(self._d[i << 1], self._d[i << 1 | 1])

    #更新クエリ
    def set(self, p, x):
        p += self._size
        self._d[p] = x
        while p:
            self._d[p >> 1] = self._op(self._d[p], self._d[p ^ 1])
            p >>= 1

    #葉を取得
    def get(self, p):
        return self._d[p + self._size]

    #取得クエリ
    def prod(self, l, r):
        sml, smr = self._e(), self._e()
        l += self._size
        r += self._size
        while l < r:
            if l & 1:
                sml = self._op(sml, self._d[l])
                l += 1
            if r & 1:
                r -= 1
                smr = self._op(self._d[r], smr)
            l >>= 1
            r >>= 1
        return self._op(sml, smr)

    #全要素の総積を取得
    def all_prod(self):
        return self._d[1]
"""
操作 op 単位元 e
最小値 min(x,y) float("inf")
最大値 max(x,y) -float("inf")
区間和 x+y 0
区間積 x*y 1
最大公約数 math.gcd(x,y) 0
"""
def op(a,b):
    return a^b
def e():
    return 0
N,Q = map(int,input().split())
A = list(map(int,input().split()))
seg = SegTree(op,e,N,A)
for i in range(Q):
    t,x,y = map(int,input().split())
    if t == 1:
        seg.set(x-1,seg.get(x-1)^y)
    if t == 2:
        print(seg.prod(x-1,y))