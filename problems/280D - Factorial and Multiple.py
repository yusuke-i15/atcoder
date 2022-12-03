from collections import defaultdict
def factorize(n):
    n_root = int(n**0.5)
    facto = defaultdict(int)
    for i in range(2,n_root+1):
        while(n%i == 0):
            facto[i] += 1
            n = n//i
    if n != 1:
        facto[n] += 1
    return facto
K = int(input())
facto = factorize(K)
ans = 0
for i in facto:
    if facto[i] == 1:
        ans = max(ans,i)
    else:
        cnt_n = 1
        cnt = 1
        while(True):
            cnt += 1
            cnt_n += 1
            tmp_cnt = cnt_n
            while(tmp_cnt%i == 0):
                tmp_cnt = tmp_cnt//i
                cnt += 1
            if cnt >= facto[i]:
                break
        ans = max(ans,cnt_n*i)      
print(ans)