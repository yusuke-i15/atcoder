def is_ok(mid,key,numbers):
    # 条件を満たすかどうか？問題ごとに定義
    if numbers[mid] >= key:
        return True
    else:
        return False

def meguru_bisect(ng, ok,key,numbers):
    '''
    初期値のng,okを受け取り,is_okを満たす最小(最大)のokを返す
    まずis_okを定義すべし
    ng ok は  とり得る最小の値-1 とり得る最大の値+1
    最大最小が逆の場合はよしなにひっくり返す
    '''
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid,key,numbers):
            ok = mid
        else:
            ng = mid
    return ok

from collections import defaultdict
H,W,rs,cs = map(int,input().split())
N = int(input())
dicR = defaultdict(list)
dicC = defaultdict(list)
for i in range(N):
    r,c = map(int,input().split())
    dicR[r].append(c)
    dicC[c].append(r)
for i in dicR:
    dicR[i].append(0)
    dicR[i].append(W+1)
    dicR[i].sort()
for i in dicC:
    dicC[i].append(0)
    dicC[i].append(H+1)
    dicC[i].sort()
ans = []
Q = int(input())
for i in range(Q):
    d,l = input().split()
    if d == "L":
        if len(dicR[rs]) == 0:
            cs = max(1,cs-int(l))
        else:
            tmp = meguru_bisect(-1,len(dicR[rs]),cs,dicR[rs])
            tmp -= 1
            cs = max(cs-int(l),dicR[rs][tmp]+1)
    if d == "R":
        if len(dicR[rs]) == 0:
            cs = min(W,cs + int(l))
        else:
            tmp = meguru_bisect(-1,len(dicR[rs]),cs,dicR[rs])
            cs = min(cs+int(l),dicR[rs][tmp]-1)
    if d == "U":
        if len(dicC[cs]) == 0:
            rs = max(1,rs - int(l))
        else:
            tmp = meguru_bisect(-1,len(dicC[cs]),rs,dicC[cs])
            tmp -= 1
            rs = max(dicC[cs][tmp]+1,rs-int(l))
    if d == "D":
        if len(dicC[cs]) == 0:
            rs = min(H,rs + int(l))
        else:
            tmp = meguru_bisect(-1,len(dicC[cs]),rs,dicC[cs])
            rs = min(dicC[cs][tmp]-1,rs+int(l))
    ans.append((rs,cs))
for i1,i2 in ans:
    print(i1,i2)