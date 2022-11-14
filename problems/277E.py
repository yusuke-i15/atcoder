from collections import deque
from collections import defaultdict
G1 = defaultdict(list)
G0 = defaultdict(list)
N,M,K = map(int,input().split())

for i in range(M):
    u,v,a = map(int,input().split())
    if a== 1:
        G1[u].append(v)
        G1[v].append(u)
    else:
        G0[u].append(v)
        G0[v].append(u)

s = list(map(int,input().split()))
S = defaultdict(int)
for i in s:
    S[i] += 1        
#dist:開始点からの距離_今回はノード0
dist1 = defaultdict(lambda: -1)
dist0 = defaultdict(lambda: -1)
dist1[1] = 0
q1 = deque()
q1.append(1)
q0 = deque()
while(True):
    while(len(q1) > 0):
        v1 = q1.popleft()
        if dist0[v1] == -1 and S[v1] != 0:
            dist0[v1] = dist1[v1]
            q0.append(v1)
        for next_v in G1[v1]:
            if dist1[next_v] == -1 or dist1[next_v] > dist1[v1]+1:
                q1.append(next_v)
                dist1[next_v] = dist1[v1] + 1
    while(len(q0) > 0):
        v0 = q0.popleft()
        if dist1[v0] == -1 and S[v0] != 0:
            q1.append(v0)
            dist1[v0] = dist0[v0]
        for next_v in G0[v0]:
            if dist0[next_v] == -1 or dist0[next_v] > dist0[v0] + 1:
                q0.append(next_v)
                dist0[next_v] = dist0[v0] + 1
    if len(q0) == 0 and len(q1) == 0:
        break
if dist1[N] == -1 and dist0[N] == -1:
    print(-1)
else:
    if dist1[N] == -1:
        print(dist0[N])
    elif dist0[N] == -1:
        print(dist1[N])
    else:
        print(min(dist1[N],dist0[N]))