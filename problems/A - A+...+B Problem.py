N,A,B = map(int,input().split())

if A>B:
    print(0)
elif A==B:
    print(1)
elif N == 1:
    if A==B:
        print(1)
    else:
        print(0)
else:
    m = N-2
    print(m*B-m*A+1)