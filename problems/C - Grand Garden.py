N = int(input())
h = list(map(int,input().split()))
h.append(0)
ans = 0
for i in range(N):
    if h[i+1] < h[i]:
        ans += h[i] - h[i+1]
print(ans) 
    