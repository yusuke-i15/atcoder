def sumtousa(a,d,n):
    return (n*(2*a + (n-1)*d))//2
N,K = map(int,input().split())
A = list(map(int,input().split()))
A.sort(reverse=True)
A.append(0)
ans = 0
if len(A) >= 2:
    cnt = 1
    for i in range(N):
        dif = A[i] - A[i+1]
        if dif*cnt <= K:
            ans += sumtousa(A[i],-1,dif)*cnt
            K -= dif*cnt
        else:
            tmp = K//cnt
            amari = K%cnt
            ans += sumtousa(A[i],-1,tmp)*cnt
            ans += (A[i] - tmp)*amari
            K = 0
        cnt += 1
        if K == 0:
            break
print(ans)