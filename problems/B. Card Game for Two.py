N = int(input())
a = list(map(int,input().split()))

a = sorted(a,reverse=True)

dif = 0
if N%2 == 1:
    dif += a[0]
    for i in range((N-1)//2):
        dif += a[(i+1)*2] - a[i*2+1]
else:
    for i in range((N)//2):
        dif += a[i*2] - a[(i+1)*2-1]
print(dif)