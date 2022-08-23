# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 21:57:50 2022

@author: 81702
"""

L,R = map(int,input().split())

min_ans = 2020


for i in range(min(R-L,2019)):
    for j in range(i,min(R-L,2019)):
        temp = ((L+i)*(L+j+1))%2019
        if temp < min_ans:
            min_ans = temp

print(min_ans)
