"""
ビット長:Bのとき以下の操作が全てO(B)
・insert(x) : 値 x を集合に（一つ）追加
・erase(x) : 値 x を集合から（一つ）削除
・lower_bound(x) : 集合内で値 x 以上の最小の要素の番号を取得. 
                    ここでの番号とは小さい方から何番目かということ.
"""
class BinaryTrie:
    def __init__(self, max_query=2*10**5, bitlen=30):
        n = max_query * bitlen
        self.nodes = [-1] * (2 * n)
        self.cnt = [0] * n
        self.id = 0
        self.bitlen = bitlen
 
    def size(self):
        return self.cnt[0]
 
    # xの個数
    def count(self,x):
        pt = 0
        for i in range(self.bitlen-1,-1,-1):
            y = x>>i&1
            if self.nodes[2*pt+y] == -1:
                return 0
            pt = self.nodes[2*pt+y]
        return self.cnt[pt]
 
    # xの挿入
    def insert(self,x):
        pt = 0
        for i in range(self.bitlen-1,-1,-1):
            y = x>>i&1
            if self.nodes[2*pt+y] == -1:
                self.id += 1
                self.nodes[2*pt+y] = self.id
            self.cnt[pt] += 1
            pt = self.nodes[2*pt+y]
        self.cnt[pt] += 1
 
    # xの削除
    # xが存在しないときは何もしない
    def erase(self,x):
        if self.count(x) == 0:
            return
        pt = 0
        for i in range(self.bitlen-1,-1,-1):
            y = x>>i&1
            self.cnt[pt] -= 1
            pt = self.nodes[2*pt+y]
        self.cnt[pt] -= 1
 
    # 昇順x番目の値(1-indexed)
    def kth_elm(self,x):
        assert 1 <= x <= self.size()
        pt, ans = 0, 0
        for i in range(self.bitlen-1,-1,-1):
            ans <<= 1
            if self.nodes[2*pt] != -1 and self.cnt[self.nodes[2*pt]] > 0:
                if self.cnt[self.nodes[2*pt]] >= x:
                    pt = self.nodes[2*pt]
                else:
                    x -= self.cnt[self.nodes[2*pt]]
                    pt = self.nodes[2*pt+1]
                    ans += 1
            else:
                pt = self.nodes[2*pt+1]
                ans += 1
        return ans
 
    # x以上の最小要素が昇順何番目か(1-indexed)
    # x以上の要素がない時はsize+1を返す
    def lower_bound(self,x):
        pt, ans = 0, 1
        for i in range(self.bitlen-1,-1,-1):
            if pt == -1: break
            if x>>i&1 and self.nodes[2*pt] != -1:
                ans += self.cnt[self.nodes[2*pt]]
            pt = self.nodes[2*pt+(x>>i&1)]
        return ans

bt = BinaryTrie()
btnokori = BinaryTrie()
N,M,K = map(int,input().split())
A = list(map(int,input().split()))
tmp = sorted(A[:M])
h = []
mv = 0
sum = 0
for i in range(K):
    bt.insert(tmp[i])
    sum += tmp[i]
for i in range(K,M):
    btnokori.insert(tmp[i])
ans = [0]*(N-M+1)
ans[0] = sum
for i in range(1,N-M+1):
    if bt.lower_bound(A[i+M-1]) > K:
        btnokori.insert(A[i+M-1])
    else:
        tmp = bt.kth_elm(K)
        bt.erase(tmp)
        btnokori.insert(tmp)
        sum -= tmp
        sum += A[i+M-1]
        bt.insert(A[i+M-1])
    if bt.count(A[i-1]) >= 1:
        bt.erase(A[i-1])
        tmp = btnokori.kth_elm(1)
        bt.insert(tmp)
        btnokori.erase(tmp)
        sum += tmp
        sum -= A[i-1]
    else:
        btnokori.erase(A[i-1])
    ans[i] = sum
print(*ans)