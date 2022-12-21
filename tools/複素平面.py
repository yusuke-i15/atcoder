#D - Opposite
#含素平面で座標変換
import math,cmath

N = int(input())
x,y = map(float,input().split())
xn2,yn2 = map(float,input().split())
p0 = complex(x,y)
pn2 = complex(xn2,yn2)
o = (p0+pn2)/2
r = cmath.rect(1,2*math.pi/N)
ans = (p0-o)*r + o
print(ans.real,ans.imag)