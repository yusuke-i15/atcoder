N = int(input())
flag = False
for i in range(N):
    a = int(input())
    if a%2 == 1:
        flag = True
print("first" if flag else "second")
"""
2 2
先手勝ち
2 2 2
先手勝ち
"""