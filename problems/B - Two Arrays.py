N = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
m = 0
p = 0
for i in range(N):
    if a[i] > b[i]:
        m += a[i]-b[i]
    elif a[i] < b[i]:
        p += (b[i]-a[i])//2
if m <= p:
    print("Yes")
else:
    print("No")