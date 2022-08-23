# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 21:49:01 2022

@author: 81702
"""

S = list(input())
a = "atcoder"

temp = 0
for i in range(7):
    for j in range(7):
        if S[j] == a[i]:
            temp += j-i
            S[i+1:j+1] = S[i:j]
            S[i] = a[i]
print(temp)

"""
catredo
8
redocta
21
"""