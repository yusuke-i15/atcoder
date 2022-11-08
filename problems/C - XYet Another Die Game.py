x = int(input())
count = x//11
amari = x%11
if amari == 0:
    print(count*2)
elif amari <= 6:
    print(count*2+1)
else:
    print(count*2+2)