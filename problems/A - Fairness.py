A,B,C,K = map(int,input().split())
dif = A-B
print(dif*(-1)**(K%2))