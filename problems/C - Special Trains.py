N = int(input())
csf = [tuple(map(int,input().split())) for i in range(N-1)]
ans = [0]*N
for i in range(N-1):
    c,s,f = csf[i]
    arrive = c+s
    for j in range(i+1,N-1):
        if arrive <= csf[j][1]:
            arrive = arrive + (csf[j][1] - arrive) + csf[j][0]
        else:
            if (arrive-csf[j][1])%csf[j][2] != 0:
                arrive = arrive + csf[j][2]-(arrive-csf[j][1])%csf[j][2] + csf[j][0]
            else:
                arrive = arrive + csf[j][0]
    print(arrive)
print(0)