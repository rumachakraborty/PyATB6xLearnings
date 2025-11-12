# # Find the first non-repeating character in a string using sets.
# # swiss -> s -x , w - Answer
#
# # print("swiss".count("s"))
# # print("swiss".count("w"))
# # print("swiss".count("i"))
# # Get only first non repeating character
# def first_non_repeating(string):
#     for char in string:
#         if string.count(char) == 1:
#
#             return char
#     return None
#
#
# print(first_non_repeating("swiss"))
# # # Using set to get all the non repeating character
# # s = set()
# #
# # def first_non_repeating(string):
# #     for char in string:
# #         if string.count(char) == 1:
# #             s.add(char)
# #             return char
# #     return None
# #
# #
# # print(first_non_repeating("swiss"))
# # print(s)

print("------------Get 2nd non repeating characters--------------")
def second_non_repeating(string):
    non_repeating_chars = [char for char in string if string.count(char) == 1]
    if len(non_repeating_chars) >= 2:
        return non_repeating_chars[1]  # second non-repeating char
    else:
        return None  # if less than 2 non-repeating chars
print(second_non_repeating("swiss"))  # Output: 'w'
print(second_non_repeating("aabbcde"))  # Output: 'd'

