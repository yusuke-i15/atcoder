n = int(input())
n_s = n

n_root = int(n**0.5)
ans = []
for i in range(2,n_root+1):
    while(n%i == 0):
        ans.append(i)
        n = n//i
if n != 1:
    ans.append(n)
print("{}:".format(n_s),*ans)