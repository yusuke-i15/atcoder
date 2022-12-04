a,b,c = map(int,input().split())
if 4*a*b< (c-a-b)**2 and c-a-b > 0:
    print("Yes")
else:
    print("No")
"""
誤差対策では
eps = 10**(-14)
A<B をA<B-epsとするテンプレがある
"""