N = int(input())
ans = 0
notten = []
for i in range(N):
    s = int(input())
    ans += s
    if s%10 != 0:
        notten.append(s)
if ans%10 != 0:
    print(ans)
elif len(notten) >= 1:
    print(ans-min(notten))
else:
    print(0)