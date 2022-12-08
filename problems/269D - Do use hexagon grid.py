from collections import defaultdict
dic_S = defaultdict(int)

N  = int(input())

black = []
B = [[0]*2001 for i in range(2001)]

for i in range(N):
    a,b = map(int,input().split())
    B[a][b] = 1
    black.append(a*10000+b)
temp = sorted(black)

count = 0
count_n = 0
temp_list = []
temp_list.append(temp[0])

for i in temp_list:
    pre = len(temp_list)
    b = i%10000
    if b > 2000:
        b = b - 10000
    b = int(b)
    a = int((i-b)/10000)
    #print("---",count_n,count,a,b)
    flag = True
    if B[a][b] == 2:
        flag = False
    if B[a][b] == 1:
        temp.remove(i)
        B[a][b] = 2
    if abs(a-1)<=1000:
        if abs(b-1)<= 1000:
            if B[a-1][b-1] == 2:
                flag = False
            elif B[a-1][b-1] == 1:
                temp.remove((a-1)*10000+b-1)
                temp_list.append((a-1)*10000+b-1)
                B[a-1][b-1] = 2
        if B[a-1][b] == 2:
            flag = False
        elif B[a-1][b] == 1:
            temp.remove((a-1)*10000+b)
            temp_list.append((a-1)*10000+b)
            B[a-1][b] = 2
    if abs(b-1)<=1000:
        if B[a][b-1] == 2:
            flag = False
        elif B[a][b-1] == 1:
            temp.remove((a)*10000+b-1)
            temp_list.append((a)*10000+b-1)
            B[a][b-1] = 2
    if abs(a+1)<=1000:
        if abs(b+1)<= 1000:
            if B[a+1][b+1] == 2:
                flag = False
            elif B[a+1][b+1] == 1:
                temp.remove((a+1)*10000+b+1)
                temp_list.append((a+1)*10000+b+1)
                B[a+1][b+1] = 2
        if B[a+1][b] == 2:
            flag = False
        elif B[a+1][b] == 1:
            temp.remove((a+1)*10000+b)
            temp_list.append((a+1)*10000+b)
            B[a+1][b] = 2
    if abs(b+1)<=1000:
        if B[a][b+1] == 2:
            flag = False
        elif B[a][b+1] == 1:
            temp.remove((a)*10000+b+1)
            temp_list.append((a)*10000+b+1)
            B[a][b+1] = 2
        
    count_n += 1
    if flag:
        count += 1
    if len(temp) == 0:
        break
    if count_n != N and len(temp_list) <= count_n:
        temp_list.append(temp[0])
print(count)

"""
4
2 1
4 1
3 2
4 2

"""