S = input()

for i in range(len(S)//2):
    s_temp = S[:len(S)-(i+1)*2]
    if s_temp[:len(s_temp)//2] == s_temp[len(s_temp)//2:]:
        print(len(s_temp))
        break