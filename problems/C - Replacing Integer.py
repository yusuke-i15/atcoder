N,K = map(int,input().split())
temp = N//K
print(min(N,N-temp*K,(temp+1)*K-N))