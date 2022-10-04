from itertools import combinations

N,K = map(int,input().split())
a = list(map(int,input().split()))
b = combinations(range(1,N),K-1)

ans = float("inf")

for i in b:
    hasi = a[0]
    temp = 0
    for k in range(1,N):
        if k in i:
            if a[k] <= hasi:
                temp += hasi - a[k] + 1
                hasi += 1
            else:
                hasi = a[k]
        elif a[k] > hasi:
            hasi = a[k]
    ans = min(ans,temp)
print(ans)