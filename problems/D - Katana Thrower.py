N,H = map(int,input().split())
a = [0]*N
b = [0]*N
for i in range(N):
    a[i],b[i] = map(int,input().split())
max_a = max(a)
b_o = []
for i in b:
    if i > max_a:
        b_o.append(i)
b_o.sort(reverse=True)
ans = 0
for i in b_o:
    H -= i
    ans += 1
    if H <= 0:
        break
if H>0:
    ans += (H+max_a-1)//max_a
print(ans)