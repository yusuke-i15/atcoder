a,b = map(int,input().split())
#複数の最大公約数
#numpy はpypyで使えないので注意
import numpy as np
x = np.array([4,16,8])
print(np.gcd.reduce(x))

#マイナスに対応していない
def gcd(a,b):
    if a == 0:
        return b
    while(b != 0):
        if a > b:
            a = a-b
        else:
            b = b-a
    return a
print(gcd(a,b))