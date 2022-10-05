N = int(input())

A = sorted(list(map(int,input().split())),reverse=True)
B = sorted(list(map(int,input().split())))
C = sorted(list(map(int,input().split())))

def is_ok_up(mid,key,temp):
    # 条件を満たすかどうか？問題ごとに定義
    if temp[mid] > key:
        return True
    else:
        return False
def is_ok_low(mid,key,temp):
    # 条件を満たすかどうか？問題ごとに定義
    if temp[mid] < key:
        return True
    else:
        return False
def meguru_bisect(ng, ok,key,temp):
    '''
    初期値のng,okを受け取り,is_okを満たす最小(最大)のokを返す
    まずis_okを定義すべし
    ng ok は  とり得る最小の値-1 とり得る最大の値+1
    最大最小が逆の場合はよしなにひっくり返す
    '''
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok_up(mid,key,temp):
            ok = mid
        else:
            ng = mid
    return ok

def meguru_bisect_rev(ng, ok,key,temp):
    '''
    初期値のng,okを受け取り,is_okを満たす最小(最大)のokを返す
    まずis_okを定義すべし
    ng ok は  とり得る最小の値-1 とり得る最大の値+1
    最大最小が逆の場合はよしなにひっくり返す
    '''
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok_low(mid,key,temp):
            ok = mid
        else:
            ng = mid
    return ok
count = 0
temp = 0
for i in range(N):
    tyudan = B[i]
    jodan = meguru_bisect_rev(-1,N-1,tyudan,A)
    if A[jodan] < tyudan:
        temp = N-jodan
    gedan = meguru_bisect(-1,N-1,tyudan,C)
    if C[gedan] > tyudan:
        temp = temp * (N-gedan)
    else:
        temp = 0
    count += temp
    temp = 0
print(count)

"""
2
3 4
1 2
3 4
"""