# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 21:50:34 2022

@author: 81702
"""

N,X,Y = map(int,input().split())



if N == 1:
    print(0)
elif N == 2:
    print(X*Y)
else:
    red_i = X*Y
    blue_i = Y
    for i in range(3,N+1):
        blue_i = red_i+blue_i*Y
        red_i = red_i + blue_i*X
    print(red_i)
#2 3 4
