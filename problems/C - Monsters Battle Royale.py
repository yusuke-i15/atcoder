import numpy as np
N = int(input())
A = list(map(int,input().split()))
print(np.gcd.reduce(A))