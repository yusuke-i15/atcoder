from collections import defaultdict
import copy
X = input()
N = int(input())
S = [input() for i in range(N)]
S_p = copy.deepcopy(S)
for j in range(len(X)):
    for i in range(len(S)):
        S[i] = S[i].replace(X[j], str(j+11))
dic = defaultdict(int)
for i in range(N):
    dic[S[i]] = S_p[i]
S.sort()
for i in range(N):
    print(dic[S[i]])