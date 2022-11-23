N = int(input())
xyh_zero = []
xyh_one = []
for i in range(N):
    x,y,h = map(int,input().split())
    if h == 0:
        xyh_zero.append((x,y,h))
    else:
        xyh_one.append((x,y,h))
for cx in range(101):
    for cy in range(101):
        if len(xyh_one) >= 1:
            H = xyh_one[0][2] + abs(xyh_one[0][0]-cx) + abs(xyh_one[0][1]-cy)
            flag = True
            for i in range(1,len(xyh_one)):
                x,y,h = xyh_one[i]
                if H != h + abs(x-cx) + abs(y-cy):
                    flag = False
                    break
            if flag:
                for i in range(len(xyh_zero)):
                    x,y,h = xyh_zero[i]
                    if max(H-abs(x-cx)-abs(y-cy),0) != h:
                        flag = False
        if flag:
            print(cx,cy,H)