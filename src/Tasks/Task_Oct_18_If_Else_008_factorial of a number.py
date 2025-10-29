# Program to calculate factorial of a number
 # Question 1. : Given a Number a number you need to calculate
# the factorial of that number # n = 5 # Fact = 5×4×3*2*1 = 120
# Fact = 0 → 1,

# Input: a number
num = int(input("Enter a number: "))

# Initialize factorial variable
fact = 1
if num <0 :
    print("Fact is not defined!")
if num ==0 :
    print("Fact is ",fact)
else:
    for i in range(1, num + 1):
        fact = fact * i

print("Factorial is  =", fact)
# Edge cases for this program
"""
Large int for Factorial
string value
alpha numeric value
decimal value
"""