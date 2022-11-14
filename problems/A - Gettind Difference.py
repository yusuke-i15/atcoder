import numpy as np
N,K = map(int,input().split())
A = list(map(int,input().split()))
M = max(A)
A = np.array(A)
gcd = np.gcd.reduce(A)
if M >= K and K%gcd == 0:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")