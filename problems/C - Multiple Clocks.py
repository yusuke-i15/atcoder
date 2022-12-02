import numpy as np
N = int(input())
T = [int(input()) for i in range(N)]
T = np.array(T)
print(np.lcm.reduce(T))