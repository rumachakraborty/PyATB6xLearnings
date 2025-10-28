# Program to calculate factorial of a number
 # Question 1. : Given a Number a number you need to calculate
# the factorial of that number # n = 5 # Fact = 5×4×3*2*1 = 120
# Fact = 0 → 1,

# Input: a number
n = int(input("Enter a number: "))

# Initialize factorial variable
fact = 1

# Factorial of 0 is defined as 1
if n == 0:
    fact = 1
else:
    # Multiply numbers from 1 to n
    for i in range(1, n + 1):
        fact = fact * i

# Output the result
print("Factorial of", n, "is:", fact)
