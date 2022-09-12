import numpy as np

N,M,C = map(int,input().split())
B = list(map(int,input().split()))
B = np.array(B)

count = 0
for i in range(N):
    A = list(map(int,input().split()))
    A = np.array(A)
    if np.dot(A,B) + C > 0:
        count += 1
print(count)
    