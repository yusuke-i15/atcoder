import math
A,B,C,D = map(int,input().split())
B_temp = B - (B//C+B//D - B//(math.lcm(C,D)))
A = A-1
A_temp = A - (A//C+A//D - A//(math.lcm(C,D)))
print(B_temp-A_temp)