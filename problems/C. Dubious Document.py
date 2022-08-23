# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 23:30:51 2022

@author: 81702
"""

from collections import defaultdict
dic_S = defaultdict(int)
    
n = int(input())

S = list(input())
for i in S:
    dic_S[i] += 1

for i in range(n-1):
    S = list(input())
    for j in dic_S:
        count = 0
        for k in range(len(S)):
            if j == S[k]: 
                count += 1
        dic_S[j] = min(count,dic_S[j])
               
temp = ""
# aからzを出力
for i in range(97, 123):
    temp = temp + chr(i)*dic_S[chr(i)]
print(temp)

"""
3
cbaa
daacc
acacac

"""