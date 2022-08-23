# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 20:33:16 2022

@author: 81702
"""
import heapq

Q = int(input())

temp_list = []
temp = 0
for i in range(Q):    
    qx = list(map(int,input().split()))
    if qx[0] == 1:
        heapq.heappush(temp_list,qx[1]-temp)
    elif qx[0] == 2:
        temp += qx[1]
    else:
        print(heapq.heappop(temp_list)+temp)

"""
5
1 3
1 5
3
2 2
3
"""