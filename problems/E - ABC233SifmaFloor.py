X = input()
ans = [0]*(len(X)+1)
tmp = 0
for i in range(len(X)):
    tmp += int(X[i])
ans[-1] = tmp%10
kuriage = 0
for i in range(1,len(X)+1):
    kuriage = (tmp+kuriage)//10
    tmp -= int(X[-i])
    ans[-(i+1)] = (tmp + kuriage)%10

for i in range(len(X)+1):
    if ans[i] != 0:
        print(*ans[i:],sep="")
        break