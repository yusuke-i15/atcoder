# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 21:41:01 2022

@author: 81702
"""

a,b = map(int,input().split())

if b-a == 1:
    print("Yes")
elif b == 10 and a == 1:
    print("Yes")
else:
    print("No")