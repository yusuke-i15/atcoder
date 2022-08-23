from collections import defaultdict
dic_S = defaultdict(int)

N = int(input())
S = list(input())

count = 0
nums = list(set(S))

for i in nums:
    dic_S = defaultdict(int)
    first_i = S.index(i)
    for second in nums:
        dic_S[second] = 30001
        for j in range(first_i+1,N):
            if S[j] == second:
                dic_S[second]=j
                break
    for second in nums:
        temp = S[dic_S[second]+1:]
        count += len(set(temp))
print(count)