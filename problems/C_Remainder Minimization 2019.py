# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 21:47:53 2022

@author: 81702
"""

S = list(input())
N = len(S)
mae = S[0:(N-1)//2]
usiro = S[(N-1)//2+1:N]

flag = True
for i in range((N-1)//2):
    if mae[i] != mae[-(i+1)]:
        flag = False
        break
    elif usiro[i] != usiro[-(i+1)]:
        flag = False
        break
if flag:
    for i in range(N):
        if S[i] != S[-(i+1)]:
            flag = False
            break

print("Yes" if flag else "No")