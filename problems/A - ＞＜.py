S = list(input())
d = [0]*(len(S)+1)
d_inv = [0]*(len(S)+1)
ans = 0
for i in range(len(S)):
    if S[i] == "<":
        d[i+1] = d[i] + 1
    else:
        d[i+1] = 0 
for i in range(len(S)-1,-1,-1):
    if S[i] == ">":
        d_inv[i] = d_inv[i+1]+1
for i in range(len(S)+1):
    ans += max(d[i],d_inv[i])
print(ans)