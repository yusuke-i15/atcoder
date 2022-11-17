N,M = map(int,input().split())
yaku = []
for i in range(1,int(M**0.5)+1):
    if M%i == 0:
        if i <= M//N:
            yaku.append(i)
        if M//i <= M//N:
            yaku.append(M//i)
yaku.sort()
print(yaku[-1])