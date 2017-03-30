list_1 = set([1,4,5,7,3,6,8,9])
list_2 = set([1,23,2,7,66,5,69])
list_3 = set([1,4,5])

print(list_1.intersection(list_2))

print(list_1.union(list_2))
print(list_1.difference(list_2))

#子集
print(list_3.issubset(list_1))
print(list_1.issuperset(list_3))
 #对称差集
print(list_1.symmetric_difference(list_3))

print("-------------")
#list_2.isdisjoint()

list_4 = set([5,6,8])
print(list_3.isdisjoint(list_4))

#交集
print(list_1 & list_2)
#并集 union
print(list_2 | list_1)
#差集 difference
print(list_1 - list_2)
#对称查集
print(list_1 ^ list_2)
#子集 subset and upperset