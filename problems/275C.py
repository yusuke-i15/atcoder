from itertools import combinations

S = list(input() for i in range(9))
borns = []
for i in range(9):
    for j in range(9):
        if S[i][j] == "#":
            borns.append((i,j))
borns.sort()
comb = combinations(borns,2)
    
ans = 0
for i in comb:
    x1,y1 = i[0]
    x2,y2 = i[1]
    q = (x2-y2+y1,y2+x2-x1)
    r = (x1-y2+y1,y1+x2-x1)
    if q in borns and r in borns:
        ans += 1
print(ans//2)