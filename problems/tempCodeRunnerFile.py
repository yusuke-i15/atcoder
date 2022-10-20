N,A,B = map(int,input().split())
ans = A*(N//(A+B))
if N%(A+B) <= A:
    ans += min(N%(A+B),A) 
print(ans)