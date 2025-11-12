squares = {x ** 2 for x in range(5)}
print(squares)
for x in range(3):
    squares.add(x**2)
    print(squares)
# Frozen Set (Immutable Set->value cannot be change)
# A frozenset cannot be changed after creation.
fset=frozenset([1,2,3,3,3,3,4]) //List converted to set
print(fset)
# my_list = [1, 2, 3, 3]
# print(fset)
# fset = frozenset(my_list)
# print(fset)
# fset.add(4) #AttributeError: 'frozenset' object has no attribute 'add'