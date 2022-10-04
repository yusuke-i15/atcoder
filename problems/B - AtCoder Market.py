N = int(input())
A = [list(map(int,input().split())) for i in range(N)]

def calc(start,goal,A):
    return abs(start-A[0]) + abs(A[1]-A[0]) + abs(A[1]-goal)


min_time = float("inf")
for i in range(N):
    start = A[i][0]
    for j in range(N):
        goal = A[j][1]
        time = 0
        for k in range(N):
            time += calc(start,goal,A[k])
        min_time = min(min_time,time)
print(min_time)