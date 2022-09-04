A,B = map(int,input().split())

count = 0
while(count*(A-1)+1<B):
    count += 1
print(count)