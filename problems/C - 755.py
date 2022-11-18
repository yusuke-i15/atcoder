from itertools import product

N = input()
N_int = int(N)
keta = len(N)
siti = ["7","5","3"]
ans = 0
for i in range(3,keta+1):
    all = product(siti,repeat = i)
    for j in all:
        if "7" not in j or "5" not in j or "3" not in j:
            continue
        tmp = "".join(j)
        tmp = int(tmp)
        if tmp <= N_int:
            ans += 1
print(ans)