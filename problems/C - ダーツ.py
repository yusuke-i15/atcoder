import bisect
def is_ok(mid,key):
    # 条件を満たすかどうか？問題ごとに定義
    if points[mid] > key:
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
N,M = map(int,input().split())
P = [0] + [int(input()) for i in range(N)]

points = []
for i in P:
    for j in P:
        points.append(i+j)

points = sorted(points)

ans = 0
for i in points:
    temp = M - i
    if temp >= 0:
        two_p = bisect.bisect(points,temp)
        ans = max(ans,points[two_p-1]+i)
print(ans)