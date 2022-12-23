N,T = map(int,input().split())
A = list(map(int,input().split()))
rA = [0]
for i in A:
    rA.append(rA[-1]+i)
amari = T%rA[-1]
for i in range(N,-1,-1):
    if amari > rA[i]:
        print(i+1,amari-rA[i])
        break