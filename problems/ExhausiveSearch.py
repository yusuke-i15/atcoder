N = int(input())
A = list(map(int,input().split()))
M = int(input())
q = list(map(int,input().split()))

for i in q:
    flag = False
    for j in range(2**N):
        sum = 0
        for k in range(N):
            if (j>>k & 1) == 1:
                sum += A[k]
        if sum == i:
            flag = True
            break
    print("yes" if flag else "no")
    