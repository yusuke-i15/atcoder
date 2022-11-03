import numpy as np
N,X = map(int,input().split())
x = list(map(int,input().split()))
x.append(X)
x = np.array(x)
x = x - np.min(x)
print(np.gcd.reduce(x))