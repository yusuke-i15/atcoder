# -*- coding: utf-8 -*-
"""
Created on Sat Jul  9 21:31:35 2022

@author: 81702
"""

S = input()
T = input()
if len(S) >= len(T) and S != T:
    flag = False
else:
    ans = [""]*(len(T)+1)
    ans[:len(T)] = T
    Si= [""]*(len(S)+1)
    Si[:len(S)] = S
    index = 0
    index_t = 0
    
    while(True):
        if ans[index+index_t] == Si[index]:
            index += 1
            if index+index_t == len(ans):
                flag = True
                break
        else:
            if Si[index-2] == Si[index-1] and Si[index-1]==ans[index+index_t]:
                index_t += 1
            else:
                flag = False
                break
print("Yes" if flag else "No")
