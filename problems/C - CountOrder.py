from itertools import permutations

N = int(input())
P = list(map(int,input().split()))
Q = list(map(int,input().split()))

R = permutations(range(1,N+1),N)
count = 0
for i in R:
    flag_a = True
    flag_b = True
    for j in range(N):
        if i[j] != P[j]:
            flag_a = False
        if i[j] != Q[j]:
            flag_b = False
    count += 1
    if flag_a:
        a = count
    if flag_b:
        b = count
print(abs(a-b))