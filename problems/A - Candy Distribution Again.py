N, x = map(int,input().split())
a = list(map(int,input().split()))
a.sort()
ans = 0
if sum(a) < x:
    print(len(a)-1)
else:
    for i in a:
        if i <= x:
            ans += 1
            x -=i
        else:
            break
    print(ans)