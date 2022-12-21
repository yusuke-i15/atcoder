from itertools import groupby
# RUN LENGTH ENCODING str -> list(tuple())
# example) 'aabbbbaaca' -> [('a', 2), ('b', 4), ('a', 2), ('c', 1), ('a', 1)]
def runLengthEncode(S: str) -> 'list[tuple(str, int)]':
    grouped = groupby(S)
    res = []
    for k, v in grouped:
        res.append((k, int(len(list(v)))))
    return res
N = int(input())
S = input()
res = runLengthEncode(S)
ans = 0
ones = 0
over = 0
for i in range(1,len(res)-1):
    k,v = res[i]
    if k == "R" and v==1:
        b,bv = res[i-1]
        a,av = res[i+1]
        if b == "A" and a == "C":
            tmp = min(av,bv)
            if tmp == 1:
                ones += 1
                ans += 1
            else:
                ans += 2
                over += tmp-2
ans += min(ones,over)
print(ans)