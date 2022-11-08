from collections import defaultdict
N = int(input())
A = list(map(int,input().split()))
set_A = list(set(A))
dic = defaultdict(int)

ans = 0
for i in A:
    dic[i] += 1
for i in set_A:
    ans  += dic[i]*(dic[i]-1)//2
ans_dic = defaultdict(int)
for i in set_A:
    temp = dic[i]
    ans_dic[i] = ans - temp*(temp-1)//2 + (temp-1)*(temp-2)//2

for i in range(N):
    print(ans_dic[A[i]])