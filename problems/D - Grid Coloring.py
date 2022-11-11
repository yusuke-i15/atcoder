from collections import defaultdict
H,W = map(int,input().split())
N = int(input())
a = list(map(int,input().split()))
A = defaultdict(int)
for i in range(N):
    A[i+1] = a[i]
ans = [[0]*W for i in range(H)]
A = dict(sorted(A.items(),key = lambda x:x[1],reverse = True))

tmp_w = 0
tmp_h = 0
for color,n in A.items():
    while(n>0):
        ans[tmp_h][tmp_w] = color
        n -= 1
        if tmp_h%2==0:
            if tmp_w+1 >= W:
                tmp_h += 1
            else:
                tmp_w += 1
        else:
            if tmp_w-1 < 0:
                tmp_h += 1
            else:
                tmp_w -= 1
for i in range(H):
    print(*ans[i])