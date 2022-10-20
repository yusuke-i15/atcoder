S = input()
ans = float("inf")
for i in range(len(S)-2):
    temp = int(S[i:i+3])
    ans = min(ans,abs(temp-753))
print(ans)