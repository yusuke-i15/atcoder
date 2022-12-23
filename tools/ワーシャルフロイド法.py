#任意の2頂点の対の最短経路を求める
#全頂点対間の最短経路をO(N^3)
#AOJ All Pairs Shortest Path
V,E = map(int,input().split())

inf = float("inf")
dist = [[inf]*V for i in range(V)]
for i in range(V):
    dist[i][i] = 0

for i in range(E):
    s,t,d = map(int,input().split())
    if dist[s][t] > d:
        dist[s][t] = d

#ワーシャルフロイド法 iからjまでの最短経路
for k in range(V):
    for i in range(V):
        for j in range(V):
            dist[i][j] = min(dist[i][j],dist[i][k]+dist[k][j])
flag = True
for i in range(V):
    if dist[i][i]<0:
        print("NEGATIVE CYCLE")
        flag = False
        break
if flag:
    for i in range(V):
        for j in range(V-1):
            print(dist[i][j] if dist[i][j] != inf else "INF",end=" ")
        print(dist[i][V-1] if dist[i][V-1] != inf else "INF")