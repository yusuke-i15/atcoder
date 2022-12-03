N = int(input())
S = list(map(int,input().split()))
A = [S[0]]
sumA = S[0]
for i in range(1,N):
    A.append(S[i]-sumA)
    sumA += A[-1]
print(*A)