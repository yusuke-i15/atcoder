N = int(input())
A = list(map(int,input().split()))
ans = 0
min = float("inf")
m_count = 0
for i in A:
    if i < 0:
        m_count += 1
    tmp = abs(i)
    if tmp < min:
        min = tmp
    ans += tmp
if m_count%2 == 0:
    print(ans)
else:
    print(ans-min*2)