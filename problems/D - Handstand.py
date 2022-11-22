from itertools import groupby
# RUN LENGTH ENCODING str -> list(tuple())
# example) "aabbbbaaca" -> [('a', 2), ('b', 4), ('a', 2), ('c', 1), ('a', 1)]
def runLengthEncode(S: str) -> "list[tuple(str, int)]":
    grouped = groupby(S)
    res = []
    for k, v in grouped:
        res.append((k, int(len(list(v)))))
    return res
N,K = map(int,input().split())
S = input()
res = runLengthEncode(S)
r = 0
zeros = 0
tmp = 0
ans = 0
for i in range(len(res)):
    while(r<len(res)):
        if res[r][0] == "0":
            if zeros+1 > K:
                break
            zeros += 1
            tmp += res[r][1]
        else:
            tmp += res[r][1]
        r += 1
    ans = max(ans,tmp)
    tmp -= res[i][1] 
    if res[i][0] == "0":
        zeros -= 1
print(ans)