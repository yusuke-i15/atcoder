while(True):
    n = int(input())
    if n == 0:
        break
    S_list = [0]*(3600*24+2)

    for i in range(n):
        start,goal = input().split()
        h,m,s = map(int,start.split(sep=":"))
        S_list[3600*h+60*m+s] += 1
        h,m,s = map(int,goal.split(sep=":"))
        S_list[3600*h+60*m+s] -= 1
    for i in range(3600*24+1):
        S_list[i+1] += S_list[i]
    print(max(S_list))