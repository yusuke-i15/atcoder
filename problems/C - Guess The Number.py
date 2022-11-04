N,M = map(int,input().split())
ans = [-1]*N
flag = True
for i in range(M):
    s,c = map(int,input().split())
    if ans[s-1] != -1 and ans[s-1] != c:
        flag = False
    else:
        ans[s-1] = c

if flag == False:
    print(-1)
elif ans[0] == 0 and N > 1:
    print(-1)
elif N == 1:
    print(max(ans[0],0))
else:
    ans_int = str(max(ans[0],1))
    for i in range(1,len(ans)):
        if ans[i] == -1:
            ans_int += str(0)
        else:
            ans_int += str(ans[i])
    print(int(ans_int))