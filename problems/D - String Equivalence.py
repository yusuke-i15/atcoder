import sys
sys.setrecursionlimit(10**9)
N = int(input())

def dfs(s,k):
    if len(s) == N:
        print(s)
    else:
        for i in range(k+1):
            dfs(s+chr(97+i),max(k,i+1))
dfs("",0)