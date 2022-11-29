import numpy as np
N = int(input())
A = list(map(int,input().split()))
cnt = [0]*(10**6+1)
for i in A:
    cnt[i] += 1

if np.all([sum(cnt[i::i])<=1 for i in range(2,10**6+1)]):
    print("pairwise coprime")
elif np.gcd.reduce(A) == 1:
    print("setwise coprime")
else:
    print("not coprime")