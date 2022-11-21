N,K = map(int,input().split())
S = input()
ans = 0
lr = 0
rl = 0
for i in range(N):
    if S[i] == "R":
        if i != 0:
            if S[i-1] == "L":
                lr += 1
        if i != N-1:
            if S[i+1] == "R":
                ans += 1
            else:
                rl += 1
    if S[i] == "L":
        if i != 0:
            if S[i-1] == "L":
                ans += 1
if min(lr,rl) >= K:
    print(min(N-1,ans+2*K))
else:
    print(min(ans+min(lr,rl)*2+K-min(lr,rl),N-1))