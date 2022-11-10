N = int(input())
N_r = int(N**0.5)
for i in range(N_r,0,-1):
    if N%i == 0:
        ans = str(N//i)
        print(len(ans))
        break
        