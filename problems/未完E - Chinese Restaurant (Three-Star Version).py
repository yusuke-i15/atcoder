from collections import defaultdict
dic_S = defaultdict(int)
import numpy as np

N = int(input())
p = list(map(int,input().split()))
S_s = [0]*len(p)

for i in range(len(p)):
    S_s[i] = (p[-i]+i)%N 
    dic_S[(p[-i]+i)%N] += 1
max_k = max(dic_S, key=dic_S.get)

temp = 0
lines = [0]*len(S_s)
i = 0

for S in S_s:
    if S > max_k:
        a = S - max_k
        if a > N -a:
            lines[i] = N-a
        else:
            lines[i] = -a
    elif S < max_k:
        a = max_k - S
        if a > N-a:
            lines[i] = -(N-a)
        else:
            lines[i] = a
    else:
        lines[i] = 0
    i += 1
lines = np.array(lines)
ave = int(np.mean(lines))
result =np.sum(np.abs(lines-ave))
print(int(result))

"""
temp = [0]*5
for S in S_s:
    a = max(S-max_k,max_k-S)
    temp[0] += min(a,N-a)
    a = max(S-max_k-1,max_k-S+1)
    temp[1] += min(a,N-a)
    a = max(S-max_k+1,max_k-S-1)
    temp[2] += min(a,N-a)
    a = max(S-max_k-2,max_k-S+2)
    temp[3] += min(a,N-a)
    a = max(S-max_k+2,max_k-S-2)
    temp[4] += min(a,N-a)
print(min(temp))
"""

"""
10
3 9 6 1 7 2 8 0 5 4
"""