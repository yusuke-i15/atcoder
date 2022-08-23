# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 20:56:44 2022

@author: 81702
"""

X,Y,N = map(int,input().split())

count = 0
amari = N%3
if Y/3 < X:
    temp = N//3
    count += temp*Y
    count += amari*X
    print(count)
else:
    print(X*N)