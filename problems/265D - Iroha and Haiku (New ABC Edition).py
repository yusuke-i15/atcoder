N,P,Q,R = map(int,input().split())
A = list(map(int,input().split()))
 
wa = [0]*(N+1)
wa[1] = A[0]
for i in range(2,N+1):
    wa[i] = wa[i-1] + A[i-1]
    
def is_ok(mid,key):
    # 条件を満たすかどうか？問題ごとに定義
    if wa[mid] >= key:
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
 
def checkL(l,i,target):
    temp = target + wa[l]
    search_result = meguru_bisect(l,i,temp)
    if wa[search_result] == temp:
        return True
    else:
        return False
def checkR(l,i,target):
    temp = wa[i] - target
    search_result = meguru_bisect(l,i,temp)
    if wa[search_result] == temp:
        return True
    else:
        return False
PQR = P+Q+R
r = N
while(True):
    temp = wa[r]- PQR
    search_result = meguru_bisect(-1,r,temp)
    if wa[search_result] != temp:
        r-=1
    else:
        if checkL(search_result,r,P) and checkR(search_result,r,R):
            print("Yes")
            break
        r -= 1
    if wa[r] <= PQR:
        print("No")
        break
"""
10 5 7 5
1 3 2 2 2 3 1 4 3 2
"""