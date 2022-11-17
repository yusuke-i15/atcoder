from collections import defaultdict
N = int(input())
xy = [tuple(map(int,input().split())) for i in range(N)]
dis = []
if N == 1:
    print(1)
else:
    for i in range(N):
        x1,y1 = xy[i]
        for j in range(i+1,N):
            x2,y2 = xy[j]
            disx = x2-x1
            disy = y2-y1
            dis.append((disx,disy))
            dis.append((-disx,-disy))
    dic = defaultdict(int)
    for i in dis:
        dic[i] += 1
    print(N - max(dic.values()))