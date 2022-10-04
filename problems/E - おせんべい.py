R,C = map(int,input().split())

a = [list(map(int,input().split())) for i in range(R)]     

max_n = 0
for i in range(2**R):
    sum_temp = 0
    re = []
    for j in range(R):
        if i >> j & 1 == 1:
            re.append(j)
    for j in range(C):
        temp = 0
        for k in range(R):
            if i >> k &1 == 1:
                temp += 1-a[k][j]
            else:
                temp += a[k][j]
        sum_temp += max(R-temp,temp)
    max_n = max(max_n,sum_temp)
print(max_n)
