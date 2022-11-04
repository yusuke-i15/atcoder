N = int(input())
A = list(map(int,input().split()))


ans = 0
temp = A[0]
up = False
down = False

for i in range(len(A)-1):
    if A[i+1] > A[i]:
        up = True
        if down:
            ans += 1
            down = False
            up = False
    if A[i+1] < A[i]:
        down = True
        if up:
            ans += 1
            up = False
            down = False
print(ans+1)