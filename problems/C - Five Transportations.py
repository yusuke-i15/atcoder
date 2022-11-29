N = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())
min_t = min(A,B,C,D,E)
ans = (N+min_t-1)//min_t
print(ans+4)