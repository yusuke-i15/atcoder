
N = int(input())

HS = [list(map(int,input().split())) for i in range(N)]

left = 0
right = 10**15

times = [0]*(N)
while(right - left > 1):
    mid = (right+left)//2
    flag = True
    
    for i in range(N):
        h,s = HS[i]
        times[i] = (mid-h)//s
    times.sort()
    for i in range(N):
        if times[i]-i < 0:
            flag = False
    if flag:
        right = mid
    else:
        left = mid
print(right)
        