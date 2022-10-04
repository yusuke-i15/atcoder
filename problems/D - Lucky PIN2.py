N = int(input())
S = list(input())

def search(A,s,target):
    if s == -1:
        return -1
    else:
        for i in range(s,len(A)):
            if A[i] == target:
                return i
        return -2

nums = list(set(S))
count = 0
for i in nums:
    first = search(S,0,i)
    for j in nums:
        second = search(S,first+1,j)
        for k in nums:
            third = search(S,second+1,k)
            if third > 0:
                count += 1
print(count)
    