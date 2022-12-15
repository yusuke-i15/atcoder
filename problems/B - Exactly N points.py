N = int(input())
ans = [N]
for i in range(1,N):
    if i*(i+1)//2 >= N:
        dif = i*(i+1)//2 - N
        ans = list(range(1,i+1))
        if dif >= 1:
            ans.remove(dif)
        break
for i in ans:
    print(i)