import numpy as np
dic_S = []
def cross(A,B):
    if A[0]*B[1] - A[1]*B[0] <= 0:
        return True
    else:
        return False

A = np.array(list(map(int,input().split()))) 
B = np.array(list(map(int,input().split())))
C = np.array(list(map(int,input().split()))) 
D = np.array(list(map(int,input().split()))) 
u = B-A
v = D-A
dic_S.append(cross(v,u))    
u = A-D
v = C-D
dic_S.append(cross(v,u))
u = B-C
v = D-C
dic_S.append(cross(u,v))
u = A-B
v = C-B
dic_S.append(cross(u,v))

if len(set(dic_S)) == 1:
    print("Yes")
else:
    print("No")