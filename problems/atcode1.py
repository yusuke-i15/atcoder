# -*- coding: utf-8 -*-
"""
Created on Sat Jul  9 20:58:33 2022

@author: 81702
"""

N,M,X,T,D = map(int,input().split())

if M >= X:
    print(T)
else:
    print(T-(X-M)*D)
