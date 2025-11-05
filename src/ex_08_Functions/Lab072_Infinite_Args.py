# def print_mul_arg(*args):
#     # args - List
#     for i in args:
#         print(i)
#
#
# print_mul_arg("rUMA")
# print_mul_arg(2, 3, 1, 4, 3, 2, 2, 2, 2, 2, 2)


def print_mul_arg(*pramod_list):
    # args - List
    for i in pramod_list:
        print(i)


print_mul_arg("rUMA")
print_mul_arg(2, 3, 1, 4, 3, 2, 2, 2, 2, 2, 2)
print_mul_arg("Ruma", "dutta")
print_mul_arg("Rum", "dutta", "third")
print_mul_arg("Ruma", "dutta", "third", 3.14)
print_mul_arg("Ruma", "dutta", "third", 3.14, True)