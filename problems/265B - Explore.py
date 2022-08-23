# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 21:04:18 2022

@author: 81702
"""


N,M,T = map(int,input().split())
A = list(map(int,input().split()))

flag = True
temp = 1
for i in range(M):
    x,y = map(int,input().split())
    A[x-1] = A[x-1] - y
for i in A:
    T = T - i
    if T<=0:
        flag = False
        break
print("Yes" if flag else "No")

"""
4 1 10
5 7 5
2 10

4 1 10
10 7 5
2 10

"""