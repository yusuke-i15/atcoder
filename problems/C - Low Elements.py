N = int(input())
P = list(map(int,input().split()))
temp = P[0]
count = 1
for i in range(1,N):
    if temp >= P[i]:
        count += 1
        temp = P[i]
print(count)