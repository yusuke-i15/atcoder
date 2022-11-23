N = int(input())
ABs = []
for i in range(N):
    a,b = map(int,input().split())
    ABs.append((a,b,a+b))
ABs.sort(key= lambda x:x[2],reverse = True)
ans = 0
for i in range(N):
    if i%2 == 0:
        ans += ABs[i][0]
    else:
        ans -= ABs[i][1]
print(ans)