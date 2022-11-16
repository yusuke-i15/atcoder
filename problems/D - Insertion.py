N = int(input())
S = input()
tmp = 0
add = 0
for i in S:
    if i == ")":
        tmp -= 1
    else:
        tmp += 1
    add = min(add,tmp)
S = "("*abs(add) + S
tmp = 0
for i in S:
    if i == ")":
        tmp -= 1
    else:
        tmp += 1
S = S + ")"*tmp
print(S)