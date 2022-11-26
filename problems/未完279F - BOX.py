from collections import defaultdict
N,Q = map(int,input().split())
dic = defaultdict(int)
change_box = defaultdict(list)
for i in range(1,N+1):
    dic[i] = i
k = N
for i in range(Q):
    op = list(map(int,input().split()))
    if op[0] == 1:
        change_box[op[2]].append((k,op[1]))
    elif op[0] == 2:
        dic[k+1] = op[1]
        k = k + 1
    else:
        if change_box[op[1]] == []:
            print(dic[op[1]]) 
        else:
            for change,k_tmp in reversed(change_box[op[1]]):
                if op[1] <= k_tmp:
                    print(change)
