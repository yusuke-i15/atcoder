from collections import defaultdict

dic_S = defaultdict(int)
dic_S[1] = 2
dic_S[3] = 1
dic_S[2] = 3
print(dic_S)
dic_S = dict(sorted(dic_S.items()))
print(dic_S)
dic_S = sorted(dic_S)
print(dic_S)
dic_S = defaultdict(int)
dic_S[1] = 2
dic_S[3] = 1
dic_S[2] = 3
dic_S = dict(sorted(dic_S.items(),key = lambda x:x[1],reverse = True))
print(dic_S)