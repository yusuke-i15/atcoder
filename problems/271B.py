from collections import defaultdict
dic_S = defaultdict(list)
N,Q = map(int,input().split())

for i in range(N):
    dic_S[i] = list(map(int,input().split()))

for i in range(Q):
    s,t = map(int,input().split())
    temp = dic_S[s-1]
    print(temp[t])
