N,K = map(int,input().split())
AB = [tuple(map(int,input().split())) for i in range(N)]
AB = sorted(AB,key=lambda x:x[0])
for a,b in AB:
    if K <= b:
        print(a)
        break
    else:
        K -= b