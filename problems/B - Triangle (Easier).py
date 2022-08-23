# -*- coding: utf-8 -*-
"""
Created on Sun Jul 31 21:15:45 2022

@author: 81702
"""
from collections import defaultdict
A = defaultdict(list)
 
N, M = map(int,input().split())
 
for i in range(M):
    u,v = map(int,input().split())
    u = u -1
    v = v-1
    A[min(u,v)].append(max(u,v))
    
count = 0
for i in range(M):
    for j in A[i]:
        for k in A[j]:
            if k in A[i]:
                count += 1
print(count)

"""
5 6
1 5
4 5
2 3
1 4
3 5
2 5
"""