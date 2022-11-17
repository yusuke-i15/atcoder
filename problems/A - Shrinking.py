s = input()
sets = set(s)
ans = float("inf")
for i in sets:
    tmp = 0
    s_tmp = s
    while(True):
        if len(set(s_tmp)) <= 1:
            break
        t = ""
        for j in range(len(s_tmp)-1):
            if s_tmp[j] == i or s_tmp[j+1] == i:
                t += i
            else:
                t += s_tmp[j]
        s_tmp = t
        tmp += 1
        
    ans = min(ans,tmp)
print(ans)