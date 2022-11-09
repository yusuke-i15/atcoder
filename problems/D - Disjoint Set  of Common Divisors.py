A,B = map(int,input().split())

def factorize(n):
    n_root = int(n**0.5)
    facto = []
    for i in range(2,n_root+1):
        while(n%i == 0):
            facto.append(i)
            n = n//i
    if n != 1:
        facto.append(n)
    return facto

A_set = set(factorize(A))
B_set = set(factorize(B))
gc = A_set & B_set | {1}
print(len(gc))