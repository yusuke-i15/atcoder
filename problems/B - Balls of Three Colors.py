T = int(input())
for i in range(T):
    rgb = list(map(int,input().split()))
    ans = float("inf")
    for i in range(3):
        if (rgb[i]-rgb[(i+1)%3])%3 == 0:
            ans = min(ans,max(rgb[i],rgb[(i+1)%3]))
    if ans != float("inf"):
        print(ans)
    else:
        print(-1)