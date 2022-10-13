from collections import deque

ans = []
while(True):
    w,h = map(int,input().split())
    if w == 0 and h == 0:
        break
    yoko = []
    tate = []

    for i in range(h-1):
        yoko.append(list(map(int,input().split())))
        tate.append(list(map(int,input().split())))
    yoko.append(list(map(int,input().split())))

    dist = [[0]*w for i in range(h)]
    dist[0][0] = 1
    q = deque()
    q.append((0,0))
    n_add = [1,-1]
    while(len(q)>0):
        v = q.popleft()
        next_x = v[0] + 1
        next_y = v[1]
        if next_x >= 0 and next_x <= w-1 and next_y >= 0 and next_y <=h-1:
            if dist[next_y][next_x] == 0 and yoko[next_y][next_x-1] == 0:
                q.append((next_x,next_y))
                dist[next_y][next_x] = dist[v[1]][v[0]] + 1
        next_x = v[0] - 1
        next_y = v[1]
        if next_x >= 0 and next_x <= w-1 and next_y >= 0 and next_y <=h-1:
            if dist[next_y][next_x] == 0 and yoko[next_y][next_x] == 0:
                q.append((next_x,next_y))
                dist[next_y][next_x] = dist[v[1]][v[0]] + 1
        next_x = v[0]
        next_y = v[1] + 1
        if next_x >= 0 and next_x <= w-1 and next_y >= 0 and next_y <=h-1:
            if dist[next_y][next_x] == 0 and tate[next_y-1][next_x] == 0:
                q.append((next_x,next_y))
                dist[next_y][next_x] = dist[v[1]][v[0]] + 1
                next_x = v[0]
        next_y = v[1] - 1
        if next_x >= 0 and next_x <= w-1 and next_y >= 0 and next_y <=h-1:
            if dist[next_y][next_x] == 0 and tate[next_y][next_x] == 0:
                q.append((next_x,next_y))
                dist[next_y][next_x] = dist[v[1]][v[0]] + 1
    ans.append(dist[h-1][w-1])
    
for i in ans:
    print(i)