K,T = map(int,input().split())
a = list(map(int,input().split()))
maxa = max(a)
if maxa <= K-maxa:
    print(0)
else:
    print(K - (K-maxa)*2-1)