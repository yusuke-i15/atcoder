from collections import defaultdict
N,x,y = map(int,input().split())
A = list(map(int,input().split()))
temp_x = [A[0]]
temp_y = [0]
for i in range((N+1)//2-1):
    temp = list(set(temp_x))
    temp_x = []
    for j in temp:
        temp_x.append(j-A[i*2+2])
        temp_x.append(j+A[i*2+2])

for i in range((N)//2):
    temp = list(set(temp_y))
    temp_y = []
    for j in temp:
        temp_y.append(j-A[i*2+1])
        temp_y.append(j+A[i*2+1])
if x in temp_x and y in temp_y:
    print("Yes")
else:
    print("No")