s = input()
K = int(input())
move = [0]*len(s)
for i in range(len(s)):
    if s[i] != "a":
        move[i] = ord("z")+1 - ord(s[i])
tmp = 0
ans = []
for i in s:
    ans.append(i)
while(K>0 and tmp<len(s)):
    if move[tmp] <= K:
        K -= move[tmp]
        ans[tmp] = "a"
    tmp += 1
if K>0:
    ans[-1] = chr(ord(ans[-1]) + K%(ord("z")-ord("a")+1))
print("".join(ans))