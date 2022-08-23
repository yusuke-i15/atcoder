# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 22:06:28 2022

@author: 81702
"""

from collections import defaultdict
N = int(input())
dic_S = defaultdict(int)
for i in range(N):
  s = input()
  dic_S[s]+=1
  if dic_S[s] == 1:
    print(s,sep="")
  else:
    print(s,"(",dic_S[s]-1,")",sep="")