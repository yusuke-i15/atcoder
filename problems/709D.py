# -*- coding: utf-8 -*-
"""
Created on Sat Jul  9 22:08:58 2022

@author: 81702
"""
import numpy as np
def check(i,j):
    d = np.linalg.norm(data[i,:2]-data[j,:2])
    rs = data[i,2]+data[j,2] 
    r_dif = abs(data[i,2]-data[j,2])
    if d <= rs and r_dif <= d:
        return True
    else:
        return False
N = int(input())
Sx,Sy,tx,ty = map(int,input().split())
data = np.empty((N,3))
S = np.array([Sx,Sy])
t = np.array([tx,ty])
ans = [] 
t_circle = []

E = list(map(lambda x: x.copy(), [[]]*N))
for i in range(N):
    a = list(map(int,input().split()))
    data[i,:] = a
    Sc = np.linalg.norm(S-a[:2])
    if Sc == a[2]:
        ans.append(i)
    tc = np.linalg.norm(t-a[:2])
    if tc == a[2]:
        t_circle.append(i)

for i in range(N):
    for j in range(i+1,N):
        if check(i,j):
            E[i].append(j)
flag = False

for i in ans:
    if i in t_circle:
        flag = True
        break
    tmp = E[i]
    for j in tmp:
        if j in t_circle:
            flag = True
            break
        for k in E[j]:
            tmp.append(k)
        

print("Yes" if flag else "No")

"""
flag = False
for i in ans:
    if i in t_circle:
        flag = True
        break
    else:
        for j in range(N):
            if j not in ans:
                if check(i,j):
                    ans.append(j)

print("Yes" if flag else "No")
"""    
    