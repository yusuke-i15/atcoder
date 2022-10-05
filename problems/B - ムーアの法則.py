import math
P = float(input())
x = 1.5*math.log2(P*math.log(2)/1.5)
print(x+P/2**(x/1.5) if x >=0 else P)