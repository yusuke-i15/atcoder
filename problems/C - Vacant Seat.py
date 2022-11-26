N = int(input())
l = 0
r = N-1
print(0)
ls = input()
if ls != "Vacant":
    print(r)
    rs = input()
    if rs != "Vacant":
        s = "start"
        while(s != "Vacant"):
            m = (l+r)//2
            print(m,l,r)
            s = input()
            if s == ls and (m - l + 1)%2 == 1:
                l = m
                ls = s
            elif s != ls and (m - l + 1)%2 == 0:
                l = m
                ls = s
            else:
                r = m
                rs = s
