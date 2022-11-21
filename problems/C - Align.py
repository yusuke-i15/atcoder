N = int(input())
A = [int(input()) for i in range(N)]
A.sort()
ans = 0
tmp = 1
n_tmp = N
while(True):
    if n_tmp == 2:
        ans += A[-tmp]
        ans -=A[-tmp-1]
        break
    ans += A[-tmp]*2
    n_tmp -= 1
    if n_tmp == 2:
        ans -= A[-tmp-1]
        ans -=A[-tmp-2]
        break
    ans -= A[tmp-1]*2
    tmp += 1
    n_tmp -= 1
ans2 = 0
n_tmp = N
tmp = 1
while(True):
    if n_tmp == 2:
        ans2 += A[-tmp]
        ans2 -=A[-tmp-1]
        break
    ans2 -= A[tmp-1]*2
    n_tmp -= 1
    if n_tmp == 2:
        ans2 += A[-tmp]
        ans2 +=A[-tmp-1]
        break
    ans2 += A[-tmp]*2
    tmp += 1
    n_tmp -= 1
print(max(ans,ans2))