# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 22:18:17 2022

@author: 81702
"""

#未完成、少なくともX以上で最小をみつけるようにする

import numpy as np


N,K = map(int,input().split())
P = list(map(int,input().split()))

omote = list(map(lambda x: x.copy(), [[]]*N))
ans = -np.ones(N)

count = []
omote[0].append(0)
count.append(1)
mim= 0
omote_n = 0
temp = P[0]
for i in range(1,N):
    print(mim)
    if temp > P[i]:
        print("min",mim)
        count[mim] += 1
        if count[mim] == K:
            ans[omote[mim]] = i
            del omote[mim]
            del count[mim]
        omote[mim].append(i)
        A = []
        while(len(omote[i])!=0):
            A.append(P[omote[i][-1]])
            i += 1
        mim = A.index(min(A))
        temp = A[mim]
    else:
        omote_n += 1
        omote[omote_n].append(i)
        temp = P[i]
        mim = omote_n
        count.append(1)
print(ans)

"""
5 2
3 5 2 1 4
"""