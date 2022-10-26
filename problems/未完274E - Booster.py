from itertools import permutations
N,M = map(int,input().split())
xypq = []
for i in range(N+M):
    x,y = map(int,input().split())
    xypq.append((x,y))

couho = permutations(range(N+M),N+M)
ans = float("inf")
for i in couho:
    temp_x = 0
    temp_y = 0
    visit = 0
    temp_ans = 0
    V = 1
    flag = True
    for j in range(N+M):
        x = xypq[i[j]][0]
        y = xypq[i[j]][1]
        temp_ans += ((x-temp_x)**2+(y-temp_y)**2)**0.5*V
        if i[j] >= N:
            V = V/2
        else:
            visit += 1
        temp_x = x
        temp_y = y
        if temp_ans > ans:
            flag = False
            break
        if visit == N:
            break
    temp_ans += (temp_x**2+temp_y**2)**0.5*V
    if flag:
        ans = min(ans,temp_ans)
    #print(i,ans,V)
print(ans)
