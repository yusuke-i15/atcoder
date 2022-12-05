from itertools import groupby
# RUN LENGTH ENCODING str -> list(tuple())
# example) "aabbbbaaca" -> [('a', 2), ('b', 4), ('a', 2), ('c', 1), ('a', 1)]
def runLengthEncode(S: str) -> "list[tuple(str, int)]":
    grouped = groupby(S)
    res = []
    for k, v in grouped:
        res.append((k, int(len(list(v)))))
    return res

S = list(input())
K = int(input())
if len(S) == 1:
    ans = K//2
else:
    ans = 0
    res = runLengthEncode(S)
    if len(res) == 1:
        ans += K*res[0][1]//2
    else:
        for i,ni in res:
            ans += K*(ni//2)
        if len(res) >= 2 and res[0][0] == res[-1][0]:
            ans -= (K-1)*(res[0][1]//2 + res[-1][1]//2 - (res[0][1]+res[-1][1])//2)
print(ans)