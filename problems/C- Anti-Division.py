from collections import defaultdict
def pf(n):
    n_root = int(n**0.5)
    ans = []
    for i in range(2,n_root+1):
        while(n%i == 0):
            ans.append(i)
            n = n//i
    if n != 1:
        ans.append(n)
    return ans
def lcm(a,b):
    a_ans = pf(a)
    b_ans = pf(b)
    sets = list(set(a_ans)|set(b_ans))
    dic_a = defaultdict(int)
    dic_b = defaultdict(int)
    for i in a_ans:
        dic_a[i] += 1
    for i in b_ans:
        dic_b[i] += 1
    ans = 1
    for i in sets:
        ans = ans*(i**max(dic_a[i],dic_b[i]))
    return ans

A,B,C,D = map(int,input().split())
B_temp = B - (B//C+B//D - B//(lcm(C,D)))
A = A-1
A_temp = A - (A//C+A//D - A//(lcm(C,D)))
print(B_temp-A_temp)