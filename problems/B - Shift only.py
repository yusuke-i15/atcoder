N = int(input())
A = list(map(int,input().split()))
ans = float("inf")
for i in A:
    temp = i
    count = 0
    while(temp%2 == 0):
        temp = temp//2
        count += 1
    ans = min(ans,count)
print(ans)