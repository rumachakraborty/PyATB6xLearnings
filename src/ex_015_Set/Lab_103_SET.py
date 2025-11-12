a = {1, 2, 3}
b = {3, 4, 5}
# print(a | b)            # {1, 2, 3, 4, 5}
# print(a.union(b))       # same result
#
#common value will take for intersection
print(a & b)            # {3}
print(a.intersection(b))
#
# print(a-b)  // it will keep which in a but not in b
# print(b-a) // it will keep which in b but not in a
#
# print(a ^ b) // symetric difference//common will remove

set1 = {1, 2, 3}
set2 = {4, 5, 6}
my_set = set1.union(set2)
print(my_set)

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

my_set = set1.intersection(set2)
print(my_set)

my_set = set1.difference(set2)
print(my_set)

my_set = set2.difference(set1)
print(my_set)









