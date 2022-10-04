S = [[""]*10 for i in range(10)]

for i in range(10):
    S[i] = input()
    
temp = []
for i in range(10):
    if "#" in S[i]:
        temp.append(i+1)
tate = []
for i in range(10):
    for j in range(10):
        if "#" in S[j][i]:
            tate.append(i+1)
print(min(temp),max(temp))
print(min(tate),max(tate))