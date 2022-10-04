from itertools import combinations

N,M = map(int,input().split())
xy = [tuple(map(int,input().split())) for i in range(M)]   

def check(Set_xy):
    q = combinations(Set_xy,2)
    for ix,iy in q:
        if (ix,iy) not in xy:
            return 0
    return len(Set_xy)
men = 1
for i in range(2**N):
    Set_xy = []
    for j in range(N):
        if i>>j & 1 == 1:
            Set_xy.append(j+1)
    men = max(men,check(Set_xy))
print(men)