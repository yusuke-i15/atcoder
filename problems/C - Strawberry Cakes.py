from collections import defaultdict
H,W,K = map(int,input().split())
s = [input() for i in range(H)]

ans = [[0]*W for i in range(H)]
k_tmp = 1
no_itigo = []
dic = defaultdict(int)
for i in range(H):
    cnt = s[i].count("#")
    if cnt >= 1:
        dic[i] += cnt
        start =  k_tmp
        for j in range(W):
            ans[i][j] = k_tmp
            if s[i][j] == "#" and k_tmp-start < cnt - 1:
                k_tmp += 1
        k_tmp += 1
    else:
        no_itigo.append(i)
for i in no_itigo:
    for j in range(1,H):
        if dic[i+j] >= 1:
            tmp = i+j
            break
        elif dic[i-j] >= 1:
            tmp = i-j
            break
    for j in range(W):
        ans[i][j] = ans[tmp][j]
for i in range(H):
    print(*ans[i])