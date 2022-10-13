N = int(input())
A = list(map(int,input().split()))
even = []
odd = []

for i in A:
    if i%2 == 0:
        even.append(i)
    else:
        odd.append(i)
ans = -1
if len(even)>=2:
    even = sorted(even,reverse=True)
    ans = max(ans,even[0]+even[1])
if len(odd) >= 2:
    odd = sorted(odd,reverse=True)
    ans = max(ans,odd[0]+odd[1])
print(ans)