n = int(input())

s = [0]*(10**6+2)
for i in range(n):
    a,b = map(int,input().split())
    s[a] += 1
    s[b+1] -= 1
for i in range(10**6+1):
    s[i+1] += s[i]
print(max(s))