s = list(input())
t = list(input())
s.sort()
t.sort(reverse = True)
s_s = ""
t_s = ""
for i in s:
    s_s += i
for i in t:
    t_s += i
ans = [s_s,t_s]
ans.sort()
if ans[0] == s_s :
    print("Yes")
else:
    print("No")