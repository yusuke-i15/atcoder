A,B = map(int,input().split())
def f(n):
    if n%2 == 0:
        tmp = n//2
        if tmp%2 == 0:
            return 0^n
        else:
            return 1^n
    else:
        tmp = (n+1)//2
        if tmp%2 == 0:
            return 0
        else:
            return 1
print(f(A-1)^f(B))