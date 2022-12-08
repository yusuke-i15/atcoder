Q = int(input())
N = 2**20
A = [-1]*N
P = list(range(N))
for i in range(Q):
    t,x = map(int,input().split())
    if t == 2:
        print(A[x%N])
    else:
        pos = x%N
        seen = [pos]
        while A[pos] != -1:
            pos = P[pos]
            seen.append(pos)
        A[pos] = x
        next = P[(pos + 1)%N]
        for j in seen:
            P[j] = next