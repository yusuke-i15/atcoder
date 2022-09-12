N = int(input())
K = int(input())
x = list(map(int,input().split()))

temp = 0
for i in range(N):
    temp += min(x[i]*2,(K-x[i])*2)
print(temp)