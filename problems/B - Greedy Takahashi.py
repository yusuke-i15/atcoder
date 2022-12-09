A,B,K = map(int,input().split())
if A >= K:
    print(A-K,B)
else:
    amari = K-A
    print(0,max(0,B-amari))