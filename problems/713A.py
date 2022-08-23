# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 21:00:37 2022

@author: 81702
"""

S = input()
temp = S[0]

if temp == S[1] and temp == S[2]:
    print(-1)
elif temp==S[1]:
    print(S[2])
elif temp == S[2]:
    print(S[1])
else:
    print(temp)
    