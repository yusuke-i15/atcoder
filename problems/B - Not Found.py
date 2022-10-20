S = list(input())
flag = True
for i in range(97, 123):
    if chr(i) not in S:
        print(chr(i))
        flag = False
        break
if flag:
    print("None")    