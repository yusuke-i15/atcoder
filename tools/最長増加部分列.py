#最長増加部分列 O(NlogN)
import bisect
def LIS_cal(seq):
    LIS = [seq[0]]
    for i in range(len(seq)):
        if seq[i] > LIS[-1]:
            LIS.append(seq[i])
        else:
            LIS[bisect.bisect_left(LIS, seq[i])] = seq[i]
    return len(LIS)

a = [1,3,5,2,4,6]
print(LIS_cal(a))