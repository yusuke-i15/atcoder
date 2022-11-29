from collections import defaultdict
N,M = map(int,input().split())
S = input()
T = input()
import math
def lcm(a,b):
    return a*b//math.gcd(a,b)
ans = lcm(N,M)
dic_s = defaultdict(str)
tmp = 1
ln = ans//N
for i in range(N):
    dic_s[tmp+ln*i] = S[i]
lm = ans//M
flag = True
for i in range(M):
    if dic_s[tmp+lm*i] != "" and dic_s[tmp+lm*i] != T[i]:
        flag = False
if flag:
    print(ans)
else:
    print(-1)