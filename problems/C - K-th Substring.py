s = input()
K = int(input())
sets = list(set(s))
sets.sort()
tmp = 0
while(K>0):
    f = sets[tmp]
    comb = [""]
    for i in range(len(s)):
        if s[i] == f:
            tmp_i = i+1
            comb.append(s[i])
            while(tmp_i<len(s)):
                comb.append(comb[-1]+s[tmp_i])
                tmp_i += 1
                if tmp_i - i >=5:
                    break
            comb = list(set(comb))
    if len(comb)-1 >= K:
        comb.sort()
        print(comb[K])
        break
    else:
        K -= len(comb) - 1
    tmp += 1