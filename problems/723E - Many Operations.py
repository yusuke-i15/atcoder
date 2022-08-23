# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 22:11:22 2022

@author: 81702
"""

N,C = map(int,input().split())

zero_results = [0]*(N)
one_results = [0]*(N)

T,A = map(int,input().split())
max_1 = 2**31 -1
if T == 1:
    zero_results[0] = 0&A
    one_results[0] = max_1&A
elif T == 2:
    zero_results[0] = 0|A
    one_results[0] = max_1|A
elif T == 3:
    zero_results[0] = 0^A
    one_results[0] = max_1^A    
for i in range(1,N):
    T,A = map(int,input().split())
    if T == 1:
        zero_results[i] = zero_results[i-1]&A
        one_results[i] = one_results[i-1]&A
    elif T == 2:
        zero_results[i] = zero_results[i-1]|A
        one_results[i] = one_results[i-1]|A
    elif T == 3:
        zero_results[i] = zero_results[i-1]^A
        one_results[i] = one_results[i-1]^A

for i in range(N):
    ones = C&one_results[i]
    zeros = ~C&zero_results[i]
    C = ones + zeros 
    print(C)
"""
3 10
3 3
2 5
1 12

"""