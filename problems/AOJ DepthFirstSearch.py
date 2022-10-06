from collections import defaultdict
G = defaultdict(list)

N = int(input())
for i in range(N):
    ukv = list(map(int,input().split()))
    for i in range(ukv[1]):
        G[ukv[0]].append(ukv[i+2])

seen = defaultdict(int)
finished = defaultdict(int)

def dfs(G,v,order):
    order += 1
    seen[v] = order
    for next_v in G[v]:
        if seen[next_v] == 0:
            order = dfs(G,next_v,order)
    order += 1
    finished[v] = order
    return order
a = 0
for i in range(1,N+1):
    if seen[i] == 0:
        a = dfs(G,i,a)
for i in range(1,N+1):
    print(i,seen[i],finished[i])