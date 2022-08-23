# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 20:29:39 2022

@author: 81702
"""

x,a,b = map(int,input().split())

if abs(x-a)<abs(x-b):
    print("A")
else:
    print("B")