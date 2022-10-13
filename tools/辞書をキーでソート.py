from collections import defaultdict

dic_S = defaultdict(int)
dic_S[1] = 2
dic_S[2] = 3
dic_S[3] = 1
print(dic_S)
dic_S = dict(sorted(dic_S.items()))
print(dic_S)