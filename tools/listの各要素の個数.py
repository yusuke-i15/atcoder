import collections

l = ['a', 'a', 'a', 'a', 'b', 'c', 'c']

c = collections.Counter(l)
print(c)
for i in c:
    print(c[i])
#多い順
print(c.most_common())
# [('a', 4), ('c', 2), ('b', 1)]