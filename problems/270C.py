N,X,Y = map(int,input().split())
from collections import defaultdict
dic_S = defaultdict(list)

if N >= 2:
    for i in range(N-1):
        u,v = map(int,input().split())
        dic_S[u].append(v)
        dic_S[v].append(u)

    temp = [X]
    def rec(node):
        if node == Y:
            for i in temp:
                print(i,end=" ")
        elif dic_S[node] != []:
            for i in dic_S[node]:
                if i not in temp:
                    temp.append(i)
                    rec(i)
            if node in temp:
                temp.remove(node)
    rec(X)
"""
7 1 7
2 3
1 3
3 4
3 5
3 6
2 7
"""
