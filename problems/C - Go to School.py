import numpy as np
N = int(input())
A = list(map(int,input().split()))
A = np.array(A)
ans = np.argsort(A)+1
print(*ans)