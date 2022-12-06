N = int(input())
L = list(map(int,input().split()))
cnt = [0]*(10**3+1)
for i in L:
    cnt[i] += 1
for i in range(1,10**3+1):
    cnt[i] = cnt[i] + cnt[i-1]
ans = 0
for i in range(N):
    for j in range(i,N):
        if i == j:
            continue
        mi = max(L[i]-L[j],L[j]-L[i])
        ma = L[i] + L[j]
        ma = min(ma,10**3+1)
        ans += cnt[ma-1] - cnt[mi]
        if L[i] > mi and L[i] < ma:
            ans -= 1
        if L[j] > mi and L[j] < ma:
            ans -= 1
print(ans//3)