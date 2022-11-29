#A以下の数がN個与えられ、全て素因数分解するとき
#O(A loglogA)
#エラトステネスの篩と同様O(A logloA)
#エラトステネスの篩で前処理huruiP(x)を使う
def huruiP(x):
    a = list(range(x+1))
    for i in range(2, int(x**0.5) + 1):
        if a[i] == i:
            a[i*i::i] = [i] * (x//i - i + 1)
    return a
def kousokuF(x,a):
    facto = []
    while(x != a[x]):
        facto.append(a[x])
        x = x//a[x]
    facto.append(x)
    return facto

#エラトステネスの篩:ｘ以下の素数
def hurui(x):
    a = [True] * (x+1)
    a[0] = a[1] = False

    for i in range(1, int(x**0.5) + 1):
        if a[i]: a[i*i::i] = [False] * (x//i - i + 1)
    r = [i for i, p in enumerate(a) if p]
    return r
a = huruiP(10)
print(huruiP(10))
print(kousokuF(6,a))