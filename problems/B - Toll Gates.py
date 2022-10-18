import numpy as np
N,M,X = map(int,input().split())
A = list(map(int,input().split()))
A = np.array(A)
ans = np.sum(np.where(A>X,1,0))
print(min(ans,len(A)-ans))