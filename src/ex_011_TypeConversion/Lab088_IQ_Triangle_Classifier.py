# Triangle Classifier:

# Write a program that classifies a triangle based on its side lengths.
# Given three input values representing the lengths of the sides,
# determine if the triangle is equilateral (all sides are equal),
# isosceles (exactly two sides are equal), or scalene (no sides are equal).
# Use an if-else statement to classify the triangle.
# Triangle Classifier with Edge Case Handling

# Input three sides
a = float(input("Enter length of side 1: "))
b = float(input("Enter length of side 2: "))
c = float(input("Enter length of side 3: "))

# Check for valid (positive) sides
if a <= 0 or b <= 0 or c <= 0:
    print("Invalid input: Side lengths must be positive numbers.")
else:
    # Check if sides can form a triangle
    if a + b > c and a + c > b and b + c > a:
        # Classify the triangle by sides
        if a == b == c:
            print("The triangle is Equilateral.")
        elif a == b or b == c or a == c:
            print("The triangle is Isosceles.")
        else:
            print("The triangle is Scalene.")
    elif a + b == c or a + c == b or b + c == a:
        print("The given sides form a Degenerate triangle (a straight line).")
    else:
        print("The given sides do not form a triangle.")
