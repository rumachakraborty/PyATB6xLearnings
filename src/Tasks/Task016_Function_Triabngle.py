# Function to determine the type of triangle
def triangle_type():
    # Take input from the user
    side1 = int(input("Enter the first side: "))
    side2 = int(input("Enter the second side: "))
    side3 = int(input("Enter the third side: "))

    # Determine the triangle type
    if side1 == side2 == side3:
        return "eq"         # Equilateral
    elif side1 == side2 or side2 == side3 or side1 == side3:
        return "iso"        # Isosceles
    else:
        return "scalene"    # Scalene

# Call the function and display the result
result = triangle_type()
print("Triangle type:", result)
