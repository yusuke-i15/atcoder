# -*- coding: utf-8 -*-
"""
Created on Sat Aug  6 21:05:25 2022

@author: 81702
"""

N = int(input())
P = list(map(int,input().split()))

count = 0
temp = P[-1]
flag = True
for i in range(N):
    if temp == 1:
        count += 1
        print(count)
        flag = False
        break
    else:
        temp = P[temp-2]
        count += 1

if flag:
    print(0)