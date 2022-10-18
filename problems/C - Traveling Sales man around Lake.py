K, N  =map(int,input().split())
A = list(map(int,input().split()))
A.append(K+A[0])
dis = [0]*(len(A)-1)
for i in range(N):
    dis[i] = A[i+1] - A[i]
print(sum(dis)-max(dis))