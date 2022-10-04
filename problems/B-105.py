N = int(input())

result = 0
for i in range(1,N+1,2):
    count = 1
    for j in range(2,i+1):
        if i%j == 0:
            count += 1
    if count == 8:
        result += 1
print(result)
