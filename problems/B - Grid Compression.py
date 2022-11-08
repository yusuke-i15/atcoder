H,W = map(int,input().split())
a = []
for i in range(H):
    ai = input()
    if "#" in ai:
        a.append(ai)
retu = []
for i in range(W):
    flag = False
    for j in range(len(a)):
        if a[j][i] == "#":
            retu.append(i)
retu = list(set(retu))
for i in a:
    for j in range(len(retu)-1):
        print(i[retu[j]],end="")
    print(i[retu[-1]])
