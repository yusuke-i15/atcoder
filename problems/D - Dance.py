#再帰だけどpypyじゃないとだめ
import sys
sys.setrecursionlimit(10**9)
from collections import defaultdict
N = int(input())
A = [list(map(int,input().split())) for i in range(2*N-1)]
seen = defaultdict(bool)

def dfs(value):
    flag = True
    for i in range(2*N):
        if not seen[i]:
            next = i
            flag = False
            break
    if flag:
        return value
    else:
        seen[next] = True
        ans = 0
        for i in range(1,2*N-next):
            if not seen[next+i]:
                seen[next+i] = True
                ans = max(ans,dfs(value^A[next][i-1]))
                seen[next+i] = False
        seen[next] = False
        return ans
print(dfs(0))