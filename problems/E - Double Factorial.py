N = int(input())

ans = 0
if N%2 == 0:
    temp = 10
    for i in range(18):
        ans += N//temp
        temp = temp*5
        ans += N//temp
        temp = temp*5
    print(ans)
else:
    print(0)
"""
ans = 1
if N%2 == 0:
    for i in range(1,(N+1)//2+1):
        ans = ans*i*2
else:
    for i in range((N+1)//2):
        ans = ans*(i*2+1)
print(ans)
count = 0
while(ans%10==0):
    count+=1
    ans = ans//10
print(count)
"""