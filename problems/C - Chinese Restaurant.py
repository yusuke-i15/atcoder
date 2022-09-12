from collections import defaultdict
dic_S = defaultdict(int)

N = int(input())
p = list(map(int,input().split()))

for i in range(len(p)):
    dic_S[(p[-i]-1+i)%N] += 1
    print((p[-i]+i)%N)
    dic_S[(p[-i]+i)%N] += 1
    dic_S[(p[-i]+1+i)%N] += 1

print(max(dic_S.values()))

"""
10
3 9 6 1 7 2 8 0 5 4
"""