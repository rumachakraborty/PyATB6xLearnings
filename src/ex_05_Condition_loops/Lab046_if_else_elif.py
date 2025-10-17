#find max between 3 numbers
#logic building
#user inputs->num1,num2,num3
#op->int or string with maximum number
num1=int(input("Enter a number: "))
num2=int(input("Enter another number: "))
num3=int(input("Enter another number: "))
"""
5,3,2
5>3 and 5>2
num1>num2 and num1>num3
num2>num1 and num2>num3
num3=max

"""

if num1>num2 and num1>num3:
    print("max" ,num1)
elif num2>num1 and num2>num3:
    print("max is" ,num2)
else:
    print("max is",num3)

