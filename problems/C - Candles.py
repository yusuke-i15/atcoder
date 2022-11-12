N,K = map(int,input().split())
x = list(map(int,input().split()))
m = []
p = []
p_s = N
for i in range(N):
    if x[i] < 0:
        m.append(x[i])
    else:
        p_s = i
        break
for i in range(p_s,N):
    p.append(x[i])
ans = float("inf")
for i in range(K-1):
    if i+1 <= len(p) and K-(i+1) <= len(m):
        ans = min(ans,p[i]-2*m[-(K-(i+1))],2*p[i]-m[-(K-(i+1))])
if len(m) >= K:
    ans = min(ans,-m[-K])
if len(p) >= K:
    ans = min(ans,p[K-1]) 
print(ans)