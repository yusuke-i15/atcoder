a,b = map(int,input().split())
if a <= 0 and b >= 0:
    print("Zero")
else:
    temp = a + min(b,0)
    if temp%2 == 0 or a > 0:
        print("Positive")
    else:
        print("Negative")