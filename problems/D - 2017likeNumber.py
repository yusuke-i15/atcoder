import numpy as np
 
# ある自然数 N が素数かどうかを判定する関数
def isprime(N):
    if N < 2:
        return False
    i = 2
    while i * i <= N:
        if N % i == 0:
            return False
        i += 1
    return True

Q = int(input())
lr = [[0]*2]*Q
for i in range(Q):
    lr[i] = list(map(int,input().split()))
 
 
lr = np.array(lr)
max_r = np.max(lr[:,1])
 
ruisekiwa = [0,0]
for i in range(2,max_r+1):
    if  i%2 == 0:
        ruisekiwa.append(ruisekiwa[-1])
    else:
        if isprime(i) and isprime((i+1)//2):
            temp = ruisekiwa[-1]+1
            ruisekiwa.append(temp)
        else:
            ruisekiwa.append(ruisekiwa[-1])
 
for i in range(Q):
    print(ruisekiwa[lr[i,1]]-ruisekiwa[lr[i,0]-1])