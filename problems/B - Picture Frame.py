H,W = map(int,input().split())
HW = [["#"]*(W+2) for i in range(H+2)]
for i in range(H):
    HW[i+1][1:W+1] = input()
for i in range(H+2):
    print(*HW[i],sep="")