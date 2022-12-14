N = int(input())
A = list(map(int,input().split()))
ruA = [0]
for i in range(N):
    if A[i] == 0:
        ruA.append(ruA[-1] - 1)
    else:
        ruA.append(ruA[-1] + 1)
tmpmax = 0
tmpmin = 0
lrmax = 0
lrmin = 0
for i in range(1,N+1):
    tmpmax = max(tmpmax,ruA[i])
    tmpmin = min(tmpmin,ruA[i])
    lrmax = max(lrmax,ruA[i]-tmpmin)
    lrmin = min(lrmin,ruA[i]-tmpmax)
print(lrmax-lrmin + 1)