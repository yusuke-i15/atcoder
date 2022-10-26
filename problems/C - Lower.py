N = int(input())
H = list(map(int,input().split()))
ans = 0
temp = 0
for i in range(1,N):
    if H[-i] <= H[-i-1]:
        temp += 1
    else:
        ans = max(ans,temp)
        temp = 0
ans = max(ans,temp)
print(ans)