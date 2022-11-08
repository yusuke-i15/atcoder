A = {1,2,3}
B = {3,4,5}
#追加
myset = set([1,2,3])
myset.add(4)
print(myset)
#削除
myset = set([1,2,3])
myset.remove(3)
print(myset)
#和集合
C = A | B
print(C)
#積集合
C = A & B
print(C)
#差集合
C = A - B
print(C)
#排他的論理和
C = A ^ B
print(C)
mylist = [11, 1, 3, 5, 3, 6, 7, 8, 9, 23, 23, 5]
myset = set(mylist)