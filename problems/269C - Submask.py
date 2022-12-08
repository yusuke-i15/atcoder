N = int(input())

one_list = []

i = 0
count = 0
temp = 1

while(True):
    if (N>>i & 1) == 1:
        one_list.append(temp)
    i += 1
    temp = 2*temp
    if temp>N:
        break

for i in range(2**len(one_list)):
    temp = 0
    for j in range(len(one_list)):
        if (i>>j & 1) == 1:
            temp += one_list[j]
    print(temp)