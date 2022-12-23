from collections import defaultdict
K = int(input())
S = input()
T = input()
a_dic = defaultdict(int)
b_dic = defaultdict(int)
for i in range(4):
    a_dic[int(S[i])] += 1
    b_dic[int(T[i])] += 1
ans = 0
for i in range(1,10):
    if (a_dic[i]+b_dic[i]) == K:
        continue
    a_dic[i] += 1
    for j in range(1,10):
        if (a_dic[j]+b_dic[j]) == K:
            continue
        b_dic[j] += 1
        a_score = 0
        b_score = 0
        for k in range(1,10):
            a_score += k*10**a_dic[k]
            b_score += k*10**b_dic[k]
        if a_score > b_score:
            if i != j:
                ans += (K-a_dic[i]-b_dic[i]+1)/(9*K-8)*(K-a_dic[j]-b_dic[j]+1)/(9*K-9)
            else:
                ans += (K-a_dic[i]-b_dic[i]+2)/(9*K-8)*(K-a_dic[j]-b_dic[j]+1)/(9*K-9)
        b_dic[j] -= 1
    a_dic[i] -= 1
print(ans)