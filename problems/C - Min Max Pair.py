# -*- coding: utf-8 -*-
"""
Created on Sun Jul 31 21:44:43 2022

@author: 81702
"""
N = int(input())
a = list(map(int,input().split()))
 
temp = 0
count = 0
for i in range(1,N+1):
    if a[i-1] == i:
        temp+=1
    elif a[a[i-1]-1]==i:
        count += 1
count = count//2
if temp>=2:
	count += temp*(temp-1)/2
print(int(count))