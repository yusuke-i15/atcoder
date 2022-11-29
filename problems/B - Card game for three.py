from collections import deque
from collections import defaultdict
dic = defaultdict(list)
dic["a"] = deque(list(input()))
dic["b"] = deque(list(input()))
dic["c"] = deque(list(input()))
tmp = "a"
while(True):
    if len(dic[tmp]) == 0:
        ans = tmp
        break
    tmp = dic[tmp].popleft()
if ans == "a":
    print("A")
elif ans == "b":
    print("B")
else:
    print("C")