# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 21:07:31 2022

@author: 81702
"""

N = int(input())

A = [[""]*N]*N
for i in range(N):
    temp = list(input())
    A[i] = temp

flag = True
for i in range(N):
    if A[i][i] != "-":
        flag = False
if flag:
    for i in range(N):
        for j in range(i,N):
            if A[i][j] == "W" and A[j][i] == "L":
                flag = True
            elif A[i][j] == "L" and A[j][i] == "W":
                flag = True
            elif A[i][j] == "D" and A[j][i] == "D":
                flag = True
            elif A[i][j] == "-" and A[j][i] == "-":
                flag = True
            else:
                flag = False
                break
        if flag == False:
            break
print("correct" if flag else "incorrect")
            
"""
4
-WWW
L-DD
LD-W
LDW-

"""