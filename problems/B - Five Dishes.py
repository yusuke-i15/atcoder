from itertools import permutations
dish = []
for i in range(5):
    dish.append(int(input()))
S = permutations(range(5),5)
ans = float("inf")
for i in S:
    temp = 0
    for j in range(4):
        temp += (dish[i[j]]+10-1)//10*10
    temp += dish[i[4]]
    ans = min(ans,temp)
print(ans)