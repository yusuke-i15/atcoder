N,K = map(int,input().split())
D = list(input().split())
for i in range(N,10**5):
    tmp = str(i)
    flag = True
    for j in D:
        if j in tmp:
            flag = False
            break
    if flag:
        print(i)
        break