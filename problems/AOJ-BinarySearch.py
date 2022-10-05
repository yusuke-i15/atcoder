n = int(input())
S = list(map(int,input().split()))
q = int(input())
T = list(map(int,input().split()))

def is_ok(mid,key):
    # 条件を満たすかどうか？問題ごとに定義
    if S[mid] >= key:
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

count = 0
for i in T:
    if i == S[meguru_bisect(-1,n-1,i)]:
        count +=1
print(count)