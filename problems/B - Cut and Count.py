N = int(input())
S = input()
ans = 0
for i in range(N):
    r = S[:i]
    l = S[i:]
    r_set = set(r)
    l_set = set(l)
    temp = r_set&l_set
    ans = max(ans,len(temp))
print(ans)