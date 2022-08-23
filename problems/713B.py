import numpy as np

N,X,Y,Z = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
A = np.array(A)
B = np.array(B)
sort_A = np.sort(A)[::-1]
goukaku = []
count = 0
for i in sort_A:
    if count == X:
        break
    for j in range(N):
        if i == A[j] and j not in goukaku:
            goukaku.append(j)
            count += 1
            if count == X:
                break

    

sort_B = np.sort(B)[::-1]
count = 0
for i in sort_B:
    if count == Y:
        break
    for j in range(N):
        if i == B[j] and j not in goukaku:
            goukaku.append(j)
            count += 1
            if count == Y:
                break
        
AB = A+B
sort_AB = np.sort(AB)[::-1]

count =  0
for i in sort_AB:
    if count == Z:
        break
    for j in range(N):
        if i == AB[j] and j not in goukaku:
            goukaku.append(j)
            count += 1
            if count == Z:
                break  
    
goukaku.sort()
for i in goukaku:
    print(i+1)