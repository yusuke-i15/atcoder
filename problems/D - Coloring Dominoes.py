mod = 10**9 + 7
N = int(input())
S1 = input()
S2 = input()
ans = 1
i = 0
pre = -1
while(i<N):
    if S1[i] != S2[i]:
        if pre == -1:
            ans = ans*6
        elif pre == 1:
            ans = ans*2
        else:
            ans = ans*3
        i += 2
        pre = 2
    else:
        if pre == -1:
            ans = ans*3
        elif pre == 1:
            ans = ans*2
        i += 1
        pre = 1
    ans = ans%mod
print(ans)