from itertools import groupby
# RUN LENGTH ENCODING str -> list(tuple())
# example) "aabbbbaaca" -> [('a', 2), ('b', 4), ('a', 2), ('c', 1), ('a', 1)]
def runLengthEncode(S: str) -> "list[tuple(str, int)]":
    grouped = groupby(S)
    res = []
    for k, v in grouped:
        res.append((k, int(len(list(v)))))
    return res

N,A,B,C,D = map(int,input().split())
S = input()
S = S[A-1:max(C,D)]

res = runLengthEncode(S)
flag = True
change_p = []
tmp = 0
change = False
for i in range(len(res)):
    if res[i][0] == "#" and res[i][1] >= 2:
        flag = False
    elif res[i][0] == "." and res[i][1] >= 3 and tmp + 2 >= B and tmp+2 <= D:
            change = True
    tmp += res[i][1]
ans = False
if C<D and flag:
    ans = True
elif C>D and flag and change:
    ans = True
print("Yes" if ans else "No")