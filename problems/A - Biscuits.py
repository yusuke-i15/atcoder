import math
def comb(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

N,P = map(int,input().split())
A = list(map(int,input().split()))
ans = 0
odd = 0
even = 0
for i in A:
    if i%2 == 0:
        even += 1
    else:
        odd += 1
if P%2 == 0:
    tmp = 0
    tmp_cnt = 0
    while(odd >= tmp):
        tmp_cnt += comb(odd,tmp)
        tmp += 2 
    ans = 2**even*tmp_cnt 
else:
    tmp = 1
    tmp_cnt = 0
    while(odd >= tmp):
        tmp_cnt += comb(odd,tmp)
        tmp += 2 
    ans = 2**even*tmp_cnt
print(ans)