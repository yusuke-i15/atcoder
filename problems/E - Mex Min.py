from collections import defaultdict
N,M = map(int,input().split())
A = list(map(int,input().split()))
dic = defaultdict(int)
for i in range(M):
    dic[A[i]] += 1
for i in range(M+2):
    if dic[i] == 0:
        ans = i
        break
for i in range(1,N-M+1):
    dic[A[i-1]] -= 1
    dic[A[i+M-1]] += 1
    if dic[A[i-1]] == 0 and A[i-1] < ans:
        ans = A[i-1]
print(ans)