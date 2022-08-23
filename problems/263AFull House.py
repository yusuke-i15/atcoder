# -*- coding: utf-8 -*-
"""
Created on Sat Aug  6 20:58:39 2022

@author: 81702
"""

a = list(map(int,input().split()))


flag2 = False
flag3 = False
for i in set(a):
    if a.count(i)==2:
        flag2 = True
    if a.count(i) == 3:
        flag3 = True
        
if flag2 and flag3:
    print("Yes")
else:
    print("No")
