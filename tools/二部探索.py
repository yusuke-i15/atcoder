# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 23:10:49 2022

@author: 81702
"""
import bisect
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

"""
meguru_biserct(左端、右端、調べたい値)
左端=-1としないと全てを調べられない
"""

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 7, 8, 9]
print(len(numbers))
a = meguru_bisect(0,8,0)
print(a,numbers[a])
a = meguru_bisect(-1,8,0)
print(a,numbers[a])
a = meguru_bisect(-1,11,8.5)
print(a,numbers[a])
a = meguru_bisect(-1,10,8.5)
print(a,numbers[a])
a = meguru_bisect(-1,9,8.5)
print(a,numbers[a])

numbers = [0,1,3]
print(meguru_bisect(-1,2,4))
print("-------------")
import time 
temp = 10**15
numbers = range(temp)
s = time.time()
print(numbers[meguru_bisect(-1,temp-1,temp/2)])
print(time.time()-s)
s = time.time()
print(numbers[bisect.bisect(numbers,temp/2)-1])
print(time.time()-s)
#bisect.bisectの方が早い?C - ダーツでTLE

"""
E - Last Rock
N = int(input())
l = 1
r = N
u = 1
d = N
yoko = False
while(True):
    if yoko == False:
        mid = (l+r)//2
        print("?",l,mid,u,d)
        T = int(input())
        if T == -1:
            break
        if mid-l+1 == T:
            l = mid + 1
        else:
            r = mid
        if l == r:
            yoko = True
            X = l
    else:
        mid = (u+d)//2
        print("?",1,N,u,mid)
        T = int(input())
        if T == -1:
            break
        if mid-u+1 == T:
            u = mid + 1
        else:
            d = mid
        if u == d:
            print("!",X,u)
            break
"""