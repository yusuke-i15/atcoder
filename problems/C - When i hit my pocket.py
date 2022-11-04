K,A,B = map(int,input().split())

if A+2 < B:
    if K >= A+1:
        K = K+1-A
        print(K//2*(B-A)+A+K%2)
    else:
        print(K+1)
else:
    print(K+1)