N,K,S = map(int,input().split())
if N == K:
    ans = [S]*N
else:
    if S == 1:
        ans = [1]*K + [2]*(N-K)
    else:
        ans = [1]
        while(K > 0):
            ans.append(S-ans[-1])
            K -= 1
        if S != 10**9:
            ans = ans + [10**9]*(N-len(ans))
        else:
            ans = ans + [10**9-2]*(N-len(ans))
print(*ans)