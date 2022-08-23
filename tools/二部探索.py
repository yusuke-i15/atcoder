# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 23:10:49 2022

@author: 81702
"""

from bisect import bisect_right, bisect_left
def is_ok(mid,key):
    # 条件を満たすかどうか？問題ごとに定義
    if numbers[mid] >= key:
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
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 7, 8, 9]
a = meguru_bisect(0,8,0)
print(a,numbers[a])
a = meguru_bisect(-1,8,0)
print(a,numbers[a])
a = meguru_bisect(0,10,9)
print(a,numbers[a])
a = meguru_bisect(0,9,9)
print(a,numbers[a])