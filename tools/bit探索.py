# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 21:32:28 2022

@author: 81702
"""
#itertools product でも
from itertools import product
for pro in product((0,1),repeat=5):
    print(pro)

def check(A):
    count_1 = 0
    while(A!=0):
        if A%2 == 1:
            count_1 += 1
            A = (A-1)/2
        else:
            A = A/2
    return count_1

# bit探索：2^N 　
def check_2(A):
    i = 0
    count = 0
    temp = 1
    while(True):
        if (A>>i & 1) == 1:
            count += 1
        i += 1
        temp = 2*temp
        if temp>A:
            return count

#Swiches
N,M = map(int,input().split())

ks = [[]]*M
for i in range(M):
    ks[i] = list(map(int,input().split()))
    
p = list(map(int,input().split()))
print(ks)
sw = [0]*M
for i in range(M):
    for j in range(ks[i][0]):
        sw[i] += 2**(ks[i][j+1]-1)

count = 0
for i in range(2**N):
    flag = True
    for j in range(M):
        temp = (sw[j]&i)
        #print(i,sw[j],temp)
        if check_2(temp)%2 != p[j]:
            flag = False
            break
    if flag:
        count += 1
print(count)

"""
5 2
3 1 2 5
2 2 3
1 0

2 2
2 1 2
1 2
0 1

5 2
3 1 2 5
2 2 3
1 0
o 8

2 3
2 1 2
1 1
1 2
0 0 1
0
"""