import numpy as np 
N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
A = np.array(A)
B = np.array(B)
A_ind = np.argsort(A)
B = B[A_ind]
ans = N
import bisect
def LIS_cal(seq):
    LIS = [seq[0]]
    for i in range(len(seq)):
        if seq[i] > LIS[-1]:
            LIS.append(seq[i])
        else:
            LIS[bisect.bisect_left(LIS, seq[i])] = seq[i]
    return len(LIS)
ans += LIS_cal(B)
print(ans)