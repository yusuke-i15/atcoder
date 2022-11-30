def is_ok(mid,key):
    # 条件を満たすかどうか？問題ごとに定義
    if ruB[mid] > key:
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

N,M,K = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
ruA = [0]
ruB = [0]
for i in range(N):
    if ruA[-1] + A[i] > K:
        break
    ruA.append(ruA[-1] + A[i])
for i in range(M):
    if ruB[-1] + B[i] > K:
        break   
    ruB.append(ruB[-1] + B[i])
a = len(ruA)
ans = 0
for i in range(a):
    nokori = K - ruA[i]
    b = meguru_bisect(-1,len(ruB),nokori) - 1
    ans = max(ans,i+b)
print(ans)
