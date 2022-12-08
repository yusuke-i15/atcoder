N = int(input())
l = 1
r = N
u = 1
d = N
yoko = False
while(True):
    if yoko == False:
        mid = (l+r)//2
        print("?",l,mid,u,d)
        T = int(input())
        if T == -1:
            break
        if mid-l+1 == T:
            l = mid + 1
        else:
            r = mid
        if l == r:
            yoko = True
            X = l
    else:
        mid = (u+d)//2
        print("?",1,N,u,mid)
        T = int(input())
        if T == -1:
            break
        if mid-u+1 == T:
            u = mid + 1
        else:
            d = mid
        if u == d:
            print("!",X,u)
            break