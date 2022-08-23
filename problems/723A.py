# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 21:02:21 2022

@author: 81702
"""

L1,R1,L2,R2 = map(int,input().split())

a = range(L2,R2)

count = 0
for i in range(L1,R1):
    if i in a:
        count += 1
print(count)
    