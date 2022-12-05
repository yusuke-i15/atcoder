T = int(input())
for i in range(T):
    N,K = map(int,input().split())
    S = list(input())
    Sk1 = 0
    S1 = 0
    ans = 0
    for i in range(K):
        if S[i] != "0":
            Sk1 += 1
    for j in range(K,N):
        if S[j] == "1":
            S1 += 1
    if Sk1 == K and S1 == 0:
        ans += 1
    for i in range(1,N-K+1):
        if S[i-1] == "1":
            Sk1 -= 1
            S1 += 1
        elif S[i-1] == "?":
            Sk1 -= 1
        if S[i+K-1] == "1":
            Sk1 += 1
            S1 -= 1
        elif S[i+K-1] == "?":
            Sk1 += 1
        if Sk1 == K and S1 == 0:
            ans += 1
    if ans == 1:
        print("Yes")
    else:
        print("No")