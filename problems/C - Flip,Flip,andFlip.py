N,M = map(int,input().split())

if N >= 2 and M >= 2:
    print((N-2)*(M-2))
else:
    print(abs(max(N,M)-2))