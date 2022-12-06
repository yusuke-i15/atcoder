N = int(input())
b = list(map(int,input().split()))
ans = []
for i in range(N):
    for j in range(len(b)-1,-1,-1):
        if b[j] == j+1:
            ans.append(j+1)
            del b[j]
            break
if len(b) == 0:
    for i in reversed(ans):
        print(i)
else:
    print(-1)