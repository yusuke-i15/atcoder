S = input()
t = "keyence"
flag = False
del_len = len(S)-len(t)
for i in range(len(S)):
    l = S[:i]
    r = S[(i+del_len):]
    if l in t and r in t:
        flag = True
print("YES" if flag else "NO")