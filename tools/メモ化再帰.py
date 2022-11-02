from functools import lru_cache
@lru_cache
def f(n):
    if n == 0:
        return 1
    return f(n // 2) + f(n // 3)
print(f(int(input())))

#辞書使う場合
from collections import defaultdict
N = int(input())
memo = defaultdict(int)
def f(n):
    if memo[n] != 0:
        return memo[n]
    if n == 0:
        return 1
    memo[n] = f(n//2)+f(n//3)
    return memo[n]
print(f(N))