N,M = map(int,input().split())
ab = [tuple(map(int,input().split())) for i in range(N)]
cd = [tuple(map(int,input().split())) for i in range(M)]
for ix,iy in ab:
    temp_check = 0
    temp_dis = float("inf")
    temp_n = 1
    for jx,jy in cd:
        if abs(ix-jx)+abs(iy-jy) < temp_dis:
            temp_dis = abs(ix-jx)+abs(iy-jy)
            temp_check = temp_n
        temp_n += 1
    print(temp_check)
