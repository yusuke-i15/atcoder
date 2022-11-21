N = int(input())
A = list(map(int,input().split()))
dif = [0]*N
for i in range(N):
    dif[i] = A[i]-(i+1)
dif.sort()
if N%2 == 0:
    b_1 = dif[N//2-1]
    b_2 = dif[N//2]
    ans = 0
    ans2 = 0
    for i in dif:
        ans += abs(i-b_1)
        ans2 += abs(i-b_2)
    ans = min(ans,ans2)
else:
    b = dif[N//2]
    ans = 0
    for i in dif:
        ans += abs(i-b)
print(ans)    