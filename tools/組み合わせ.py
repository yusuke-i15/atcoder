import itertools
from itertools import combinations

M = 3
comb = combinations(range(M),2)


#重複あり
all = list(itertools.combinations_with_replacement('abc', 2))
print(len(all))

import itertools
import pprint
l1 = ['a', 'b', 'c']
l2 = ['X', 'Y', 'Z']
p = itertools.product(l1, l2)
for v in p:
    print(v)