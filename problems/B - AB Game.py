N,A,B = map(int,input().split())
def f(x):
    return x//A*min(A,B) + min(x%A,B-1)
print(max(f(N)-f(A-1),0))