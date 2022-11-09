#条件を満たす連続区間を全て求められる。区間の左と右の2つを数列の端から端まで動かすことで、計算量はO(n)
#下の例ではfor文で左端、whileで右端を移動させている

#D - Enough Array
N,K = map(int,input().split())
a = list(map(int,input().split()))

r = 0
ans = 0
sum_tmp = 0
for i in range(N):
    while(r<=N):
        if sum_tmp >= K:
            ans += N-r+1
            break
        if r==N:
            break
        sum_tmp += a[r]
        r += 1
    sum_tmp -= a[i]
print(ans)