from itertools import permutations        

N = 8
k = int(input())
r = [0]*k
c = [0]*k

def check_Q(temp):

    for i in range(N):
        xp = temp[i][0]
        xn = temp[i][0]
        yp = temp[i][1]
        yn = temp[i][1]
        for j in range(N):
            yp += 1
            yn -= 1
            xp += 1
            xn -= 1
            if (xp,yp) in temp or (xn,yp) in temp or (xp,yn) in temp or (xp,yp) in temp:
                return False
    return True

def plot_Q(temp):
    for i in range(N):
        for j in range(N-1):
            q = (i,j)
            if q in temp:
                print("Q",end="")
            else:
                print(".",end="")
        q = (i,N-1)
        if q in temp:
            print("Q")
        else:
            print(".")
    

for i in range(k):
    r[i],c[i] = map(int,input().split())
r_nokori = list(set(range(N)) - set(r))
c_nokori = list(set(range(N)) - set(c))
R = permutations(range(N-k),N-k)
banmen = [["."]*N for i in range(N)]
Qs = [(0,0) for i in range(N)]
for i in range(k):
    banmen[r[i]][c[i]] = "Q"
    Qs[i] = (r[i],c[i])

for i in R:
    temp = Qs
    for j in range(N-k):
        temp[j+k] = (r_nokori[j],c_nokori[i[j]])
    if check_Q(temp):
        plot_Q(temp)
        break
