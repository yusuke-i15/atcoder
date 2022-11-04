from collections import defaultdict
N = int(input())
memo = defaultdict(int)
memo[0] = 1
memo[1] = 2
def f(n):
    if memo[n] != 0:
        return memo[n]
    if n == 0:
        return 1
    memo[n] = f(n//2)+f(n//3)
    return memo[n]
print(f(N))