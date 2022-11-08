H,W = map(int,input().split())
s = [["."]*(W+2) for _ in range(H+2)]
for i in range(1,H+1):
    s[i][1:W+1] = input()
flag = True
for i in range(1,H+1):
    for j in range(1,W+1):
        if s[i][j] == "#":
            if s[i+1][j] == "." and s[i][j+1] == "." and s[i-1][j] == "." and s[i][j-1] == ".":
                flag = False
print("Yes" if flag else "No")