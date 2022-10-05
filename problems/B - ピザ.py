def is_ok(mid,key):
    # 条件を満たすかどうか？問題ごとに定義
    if tenpo[mid] > key:
        return True
    else:
        return False
def is_ok2(mid,key):
    # 条件を満たすかどうか？問題ごとに定義
    if tenpo_han[mid] > key:
        return True
    else:
        return False


def meguru_bisect(ng, ok,key):
    '''
    初期値のng,okを受け取り,is_okを満たす最小(最大)のokを返す
    まずis_okを定義すべし
    ng ok は  とり得る最小の値-1 とり得る最大の値+1
    最大最小が逆の場合はよしなにひっくり返す
    '''
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid,key):
            ok = mid
        else:
            ng = mid
    return ok
def meguru_bisect2(ng, ok,key):
    '''
    初期値のng,okを受け取り,is_okを満たす最小(最大)のokを返す
    まずis_okを定義すべし
    ng ok は  とり得る最小の値-1 とり得る最大の値+1
    最大最小が逆の場合はよしなにひっくり返す
    '''
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok2(mid,key):
            ok = mid
        else:
            ng = mid
    return ok

d = int(input())
n = int(input())
m = int(input())
tenpo = [0]*n
tenpo_han = [0]*n
for i in range(1,n):
    tenpo[i] = int(input())
    tenpo_han[-i] = d - tenpo[i]
ans = 0
tenpo = sorted(tenpo)
tenpo_han = sorted(tenpo_han)
for i in range(m):
    k = int(input())
    if k >= tenpo[-1]:
        ans_tokei = k-tenpo[-1]
    else:    
        tokei = meguru_bisect(-1,n-1,k)
        ans_tokei= k - tenpo[tokei-1]
    if d-k >= tenpo_han[-1]:
        ans_han = d-k-tenpo_han[-1]
    else:
        han = meguru_bisect2(-1,n-1,d-k)
        ans_han = d-k - tenpo_han[han-1]
    ans += min(ans_tokei,ans_han)
print(ans)
"""
meguru_biserct(左端、右端、調べたい値)
左端=-1としないと全てを調べられない
"""