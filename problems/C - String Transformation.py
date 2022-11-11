from collections import defaultdict
S = input()
T = input()
dic_S = defaultdict(int)
dic_T = defaultdict(int)
for i in range(len(S)):
    dic_S[S[i]] += 1
    dic_T[T[i]] += 1
s_l = []
t_l = []
for i in set(S):
    s_l.append(dic_S[i])
for i in set(T):
    t_l.append(dic_T[i])
s_l.sort()
t_l.sort()
if s_l == t_l:
    print("Yes")
else:
    print("No")