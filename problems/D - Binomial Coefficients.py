n = int(input())
a = list(map(int,input().split()))
N = max(a)
r = (N+1)//2
r_u = []
r_l = []
for i in a:
    if i == N:
        continue
    elif i>=r:
        r_u.append(i)
    else:
        r_l.append(i)
r_u.sort()
r_l.sort()
if len(r_u) == 0:
    print(N,r_l[-1])
elif len(r_l) == 0:
    print(N,r_u[0])
elif abs(r-r_u[0]) <= abs(r-r_l[-1]):
    print(N,r_u[0])
else:
    print(N,r_l[-1])