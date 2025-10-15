# Task for the Day
# Take 2 input from the user
# print the reminder and quotient
# 15->num1
# 2->num2
# Q->7
# R->1
from argparse import REMAINDER

num1=int(input("Enter First number: "))
num2=int(input("Enter 2nd number: "))
quotient=num1//num2
reminder=num1%num2

print(quotient)
print(reminder)