a,b = map(int,input().split())
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