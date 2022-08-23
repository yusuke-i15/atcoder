# -*- coding: utf-8 -*-
"""
Created on Sat Aug  6 21:26:13 2022

@author: 81702
"""

N,L,R = map(int,input().split())
A = list(map(int,input().split()))

ruisekiA = [0]*(N+1)
ruisekiA[1] = min(L,A[0])
for i in range(1,N):
    ruisekiA[i+1] = min(L*(i+1),ruisekiA[i]+A[i])

ruisekiR = [0]*(N+1)
ruisekiR[1] = min(R,A[-1])
for i in range(1,N):
    ruisekiR[i+1] = min(R*(i+1),ruisekiR[i]+A[-(i+1)])

temp = ruisekiA[-(N+1)]+ruisekiR[N]
for i in range(N):
    temp = min(temp,ruisekiA[-(i+1)]+ruisekiR[i])
print(temp)
"""
10 -5 -3
9 -6 10 -1 2 10 -1 7 -15 5
"""