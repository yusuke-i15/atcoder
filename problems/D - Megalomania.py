N = int(input())
AB = [tuple(map(int,input().split())) for i in range(N)]
yoyuu = []
for i in range(N):
    yoyuu.append((i,AB[i][1]))
yoyuu.sort(key=lambda x:x[1])
flag = True
t = 0
for i in range(N):
    tmp = yoyuu[i][0] 
    t += AB[tmp][0]
    if t > AB[tmp][1]:
        flag = False
print("Yes" if flag else "No")
    