# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 21:17:35 2022

@author: 81702
"""

from collections import defaultdict
dic_S = defaultdict(int)

H,W = map(int,input().split())

grid = [[""]*W for i in range(H)]

for i in range(H):
    grid[i] = list(input())

temp = grid[0][0]
i = 1
j = 1
while(True):
    if temp == "R" and j != W:
        j = j + 1
    elif temp == "L" and j != 1:
        j = j - 1
    elif temp == "U" and i != 1:
        i = i - 1
    elif temp == "D" and i != H:
        i = i + 1
    else:
        print(i,j)
        break
    temp = grid[i-1][j-1]
    dic_S[1000*i+j] += 1
    if dic_S[1000*i+j] == 2:
        print(-1)
        break

"""
2 3
RDU
LRU

2 3
RRD
ULL

"""