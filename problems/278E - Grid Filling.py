from collections import defaultdict
import copy
H,W,N,h,w = map(int,input().split())
A = [list(map(int,input().split())) for i in range(H)]
dic = defaultdict(int)
for i in range(H):
    for j in range(W):
        dic[A[i][j]] += 1
ans = len(dic)
ans_A = [[0]*(W-w+1) for i in range(H-h+1)]
tmp = 0
for i in range(H-h+1):
    for j in range(W-w+1):
        if i == 0 and j == 0:
            for k in range(i,i+h):
                for l in range(j,j+w):
                    dic[A[k][l]] -= 1
                    if dic[A[k][l]] == 0:
                        tmp += 1
            dic_n = copy.deepcopy(dic)
            tmp_n = tmp
        elif j == 0:
            dic = copy.deepcopy(dic_n)
            tmp = tmp_n
            for k in range(j,j+w):
                dic[A[i-1][k]] += 1
                if dic[A[i-1][k]] == 1:
                    tmp -= 1
            for k in range(j,j+w):
                dic[A[i+h-1][k]] -= 1
                if dic[A[i+h-1][k]] == 0:
                    tmp += 1
            dic_n = copy.deepcopy(dic)
            tmp_n = tmp
        else:
            for k in range(i,i+h):
                dic[A[k][j-1]] += 1
                if dic[A[k][j-1]] == 1:
                    tmp -= 1
            for k in range(i,i+h):
                dic[A[k][j+w-1]] -= 1
                if dic[A[k][j+w-1]] == 0:
                    tmp += 1
        ans_A[i][j] = ans - tmp
for i in range(H-h+1):
    print(*ans_A[i])