from itertools import product
S = input()

ans = 0
for pro in product((0,1),repeat=len(S)-1):
    tmp = 0
    tmp2 = 0
    for i in range(len(S)-1):
        tmp += int(S[i])
        if pro[i] == 0:
            tmp = tmp*10
        else:
            tmp2 += tmp
            tmp = 0
    ans += tmp + tmp2 + int(S[-1])
print(ans)