# -*- coding: utf-8 -*-
"""
Created on Sun Jul 31 21:00:50 2022

@author: 81702
"""

Y = int(input())

temp = Y%4

if temp == 2:
    print(Y)
elif temp == 3:
    print(Y+3)
elif temp == 0:
    print(Y+2)
elif temp == 1:
    print(Y+1)