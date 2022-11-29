N = int(input())
X = list(map(int,input().split()))
sort_X = sorted(X)
m1 = sort_X[N//2-1]
m2 = sort_X[N//2]
for i in range(N):
    if X[i]<=m1:
        print(m2)
    else:
        print(m1)