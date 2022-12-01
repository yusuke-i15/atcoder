N = int(input())
S = set()
T = set()
for i in range(N):
    s = input()
    for j in range(N):
        if s[j] == "#":
            S.add((i,j))
for i in range(N):
    t = input()
    for j in range(N):
        if t[j] == "#":
            T.add((i,j))
flag = False
for i in range(4):
    sx,sy = min(S)
    tx,ty = min(T)
    
    tmpS = set()
    tmpT = set()
    for x,y in S:
        tmpS.add((x-sx,y-sy))
    for x,y in T:
        tmpT.add((x-tx,y-ty))
    if tmpS == tmpT:
        flag = True
    T = set((y,-x) for x,y in T)
print("Yes" if flag else "No")