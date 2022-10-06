import itertools
from itertools import combinations

M = 3
comb = combinations(range(M),2)


#重複あり
all = list(itertools.combinations_with_replacement('abc', 2))
print(len(all))