
#整数÷整数で切り捨て
print(3//2)
print(3//2.0)
print("------------")
#計算結果（非整数でも）切り捨て
print(int(3//2.0))
print("------------")
#切り上げ
M = 5
N = 2
print((M+N-1)//N)
print(int((M+N-1)//N))
print("------------")

print(-(-M//N))

#四捨五入
print(int(round(2.50000000000001)))