def is_ok(mid,key):
    # 条件を満たすかどうか？問題ごとに定義
    if field[mid] >= key:
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
from collections import defaultdict
N,K = map(int,input().split())
P = list(map(int,input().split()))
field = []
cnt = defaultdict(list)
ans = [-1]*N
t = 1
if K >= 2:
    for i in P:
        key = meguru_bisect(-1,len(field),i)
        if key >= len(field):
            field.append(i)
            cnt[i].append((1,i))
        else:
            cnt[i].append((cnt[field[key]][0][0] + 1,field[key]))
            if cnt[i][0][0] >= K:
                ans[i-1] = t
                tmp = cnt[i][0][1]
                while(cnt[tmp][0][1] != tmp):
                    ans[tmp-1] = t
                    tmp = cnt[tmp][0][1]
                ans[tmp-1] = t
                del field[key]
            else:
                field[key] = i
        t += 1
else:
    t = 1
    for i in P:
        ans[i-1] = t
        t += 1 
for i in ans:
    print(i)
    