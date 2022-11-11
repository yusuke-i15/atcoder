from collections import defaultdict
import numpy as np
N,M = map(int,input().split())
dic = defaultdict(list)
for i in range(M):
    p,y = map(int,input().split())
    dic[p].append((y,i))
ans = [[0]*2 for i in range(M)]
for i in range(1,N+1):
    tmp = np.array(dic[i])
    if tmp.size > 0:
        sor = np.argsort(tmp[:,0],axis=0)
        tmp[sor,0] = np.arange(1,tmp[:,0].size+1)
        for j in range(tmp[:,0].size):
            ans[tmp[j,1]][0] = i
            ans[tmp[j,1]][1] = tmp[j,0]
for i in range(M):
    print(str(ans[i][0]).zfill(6),end="")
    print(str(ans[i][1]).zfill(6))