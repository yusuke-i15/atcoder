N = int(input())
a = list(map(int,input().split()))
colors = []
over = 0
for i in a:
    for j in range(1,9):
        if i <= j*400 - 1:
            colors.append(j)
            break
    if i >= 3200:
        over += 1
colors = set(colors)
if len(colors) == 0:
    print(1,end =" ")
else:
    print(len(colors),end=" ")
print(len(colors)+over)