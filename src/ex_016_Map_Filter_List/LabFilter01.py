nums = [1, 2, 3, 4, 5, 6]


def even_num(x):
    return x % 2 == 0

print(even_num(20))
print(even_num(21))
print("---------------------------------")
print_even_numbers = list(filter(even_num, nums))
print(print_even_numbers)

print("---------How filter works------------------------")
list_student = [50, 51, 100,10,20,35,45,50,99,100]


def keep(x):
    if x >= 50:
        return True


all_student = list(filter(keep,list_student))
print(all_student)