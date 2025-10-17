#print to find the max between two numbers
#Logic building
"""
1.user inputs->2 integer
2.o/p->int 1 which ever is greater max number it will return
.
"""
num1=float(input("Enter a number: "))
num2=float(input("Enter another number: "))


if num1>0 and num2>0:
    print("number should be positive")
if num1 >= num2:
    print("maximum", num1)
else:
    print("maximum" ,num2)
