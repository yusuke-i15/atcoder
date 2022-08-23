# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 21:43:46 2022

@author: 81702
"""

N = int(input())
A = list(map(int,input().split()))
temp = []
for i in range(N):
    if A[i] not in temp:
        temp.append(A[i])
print(len(temp))

"""
6
1 4 1 2 2 
11
3 1 4 1 5 9 2 6 5 3 5

"""