N = int(input())
a = list(map(int,input().split()))
rua = [0]
for i in a:
    rua.append(rua[-1]+i)
ans = float("inf")
for i in range(1,N):
    ans = min(ans,abs(rua[i]-(rua[N]-rua[i])))
print(ans)