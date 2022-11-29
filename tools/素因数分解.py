#O(n^0.5)
n = int(input())
n_s = n

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
print("{}:".format(n_s),*factorize(n))