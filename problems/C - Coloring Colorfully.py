S = input()
count = 0
for i in range(len(S)):
    if S[i] == "0" and i%2 == 0:
        count += 1
    if S[i] == "1" and i%2 == 1:
        count += 1
print(min(count,len(S)-count))