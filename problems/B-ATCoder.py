S = input()

acgt = ["A","C","G","T"]

count = 0
temp = 0
for i in S:
    if i in acgt:
        temp += 1
    else:
        count = max(count,temp)
        temp = 0
count = max(count,temp)
print(count)