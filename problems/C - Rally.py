import numpy as np
N = int(input())
X = np.array(list(map(int,input().split())))
P = np.average(X)
P = (P*2+1)//2
print(int(np.sum(np.square(X-P))))