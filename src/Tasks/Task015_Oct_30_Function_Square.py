# Program to calculate the square of a number
# Take input from the user
# num = float(input("Enter a number: "))
# # Calculate the square
# square = num ** 2
# # Display the result
# print(f"The square of {num} is {square}")

print("-----------------Function create----------------------------")
# Function to calculate the square of a number
def square_number(num):
    return num ** 2

# Main part of the program
number = float(input("Enter a number: "))
result = square_number(number)

print(f"The square of {number} is {result}")
square_number(3)
print("-----------------call function----------------------------")
square_number(3)
square_number(10)
square_number(2)
square_number(5)