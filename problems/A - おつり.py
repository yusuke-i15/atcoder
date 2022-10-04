n = int(input())
count = 0
coin = [500,100,50,10,5,1]
x = 1000-n
for i in coin:
    if x >= i:
        count += x//i
        x = x%i
print(count)