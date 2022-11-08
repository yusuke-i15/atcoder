R,G,B,N = map(int,input().split())
ans = 0
for i in range(N//R+1):
    for j in range(N//G+1):
        if (N-i*R-j*G)%B == 0 and N-i*R-j*G >=0:
            ans += 1
print(ans)