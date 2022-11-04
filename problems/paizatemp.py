# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
import copy
N = int(input())
a = [list(map(int,input().split())) for i in range(N)]
r,c,s,d = map(int,input().split())
ans = copy.deepcopy(a)
r = r-1
c = c-1
if d == 90:
    while(s>1):
        for i in range(s):
            ans[r][c+i] = a[r+s-1-i][c]
        for i in range(1,s):
            ans[r+i][c+s-1] = a[r][c+i]
        for i in range(1,s):
            ans[r+s-1][c+s-1-i] = a[r+i][c+s-1]
        for i in range(1,s-1):
            ans[r+s-1-i][c] = a[r+s-1][c+i]
        s = s-2
        r = r+1
        c = c+1
if d == 270:
    while(s>1):
        for i in range(s):
            ans[r+s-1-i][c] = a[r][c+i]
        for i in range(1,s):
            ans[r][c+i] = a[r+i][c+s-1]
        for i in range(1,s):
            ans[r+i][c+s-1] = a[r+s-1][c+s-1-i]
        for i in range(1,s-1):
            ans[r+s-1][c+i] = a[r+i][c]
        s = s-2
        r = r+1
        c = c+1
if d == 180:
    while(s>1):
        for i in range(s):
            ans[r][c+i] = a[r+s-1][c+s-1-i]
        for i in range(1,s):
            ans[r+i][c+s-1] = a[r+s-1-i][c]
        for i in range(1,s):
            ans[r+s-1][c+s-1-i] =a[r][c+i]
        for i in range(1,s-1):
            ans[r+s-1-i][c] = a[r+i][c+s-1]
        s = s-2
        r = r+1
        c = c+1
for i in range(N):
    for j in range(N-1):
        print(ans[i][j],end=" ")
    print(ans[i][N-1])