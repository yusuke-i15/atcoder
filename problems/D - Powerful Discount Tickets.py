import heapq

N,M = map(int,input().split())
A = list(map(lambda x: int(x)*(-1),input().split()))
heapq.heapify(A)

for i in range(M):
    tmp_min = heapq.heappop(A)
    heapq.heappush(A,-tmp_min//2*(-1))
print(-sum(A))