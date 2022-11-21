N = int(input())

ans = []
for h in range(1,3501):
    for n in range(1,3501):
        tmp = 4*h*n-N*n-N*h
        if tmp == 0:
            continue
        w = N*h*n/tmp
        if w.is_integer() and w <=3500 and w >= 1:
            ans.append((h,n,int(w)))
            break
print(*ans[0])