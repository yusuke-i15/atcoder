N,W = map(int,input().split())
time = [0]*(2*10**5+2)
for i in range(N):
    s,t,p = map(int,input().split())
    time[s] += p
    time[t] -= p
flag = True
for i in range(2*10**5+1):
    if time[i] > W:
        flag = False
    time[i+1] += time[i]
print('Yes' if flag else 'No')