from collections import defaultdict
N,X,M = map(int,input().split())
dic = defaultdict(list)
dic[1].append((1%M,1,1))
dic[0].append((0,0,float("inf")))
for i in range(2,M):
    cnt = 0
    sum = 0
    tmp = i
    while(tmp<M):
        cnt += 1
        sum += tmp
        tmp *= tmp
    dic[i].append((tmp%M,sum,cnt))
ans = 0
seen = defaultdict(int)
loop_flag = False
while(N>0):
    if X == 0:
        break
    amari,s,c = dic[X][0]
    if c <= N:
        if loop_flag:
            cs += c
            loop_sum += s
        else:
            ans += s
            N -= c
    else:
        for i in range(N):
            ans += X
            N -= 1
            tmp = X**2%M
    X = amari
    if seen[X] == 1:
        if loop_flag:
            loop = N//cs
            ans += loop*loop_sum
            N = N - loop*cs
            loop_flag = False
            seen = defaultdict(int)
        else:
            loop_flag = True
            loop_sum = 0
            seen = defaultdict(int)
            cs = 0
    seen[X] += 1
print(ans)