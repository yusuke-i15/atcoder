from collections import defaultdict
import heapq

n,k = map(int,input().split())

G = defaultdict(list)
V = 0
for i in range(k):
    temp = list(map(int,input().split()))
    if temp[0] == 1:
        G[temp[1]].append((temp[2],temp[3]))
        G[temp[2]].append((temp[1],temp[3]))
        V += 1
    else:
        seen = defaultdict(bool)
        dist = defaultdict(lambda: 10**10)
        dist[temp[1]] = 0
        q = [(0,temp[1])]
        heapq.heapify(q)
        while(len(q)>0):
            v = heapq.heappop(q)[1]
            seen[v] = True
            for next in G[v]:
                if not seen[next[0]] and dist[next[0]] > dist[v] + next[1]:
                    dist[next[0]] = dist[v] + next[1]
                    heapq.heappush(q,(dist[next[0]],next[0]))
        if dist[temp[2]] != 10**10:
            print(dist[temp[2]])
        else:
            print(-1)