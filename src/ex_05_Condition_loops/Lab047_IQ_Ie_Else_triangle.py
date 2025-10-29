"""
Write a program that classifies a triangle based on its side lengths.
 Given three input values representing the lengths of the sides,
 determine if the triangle is equilateral (all sides are equal),
  isosceles (exactly two sides are equal), or scalene (no sides are equal).
Use an if-else statement to classify the triangle.
"""

# Triangle Type Classifier

# Get input for the three sides
a = float(input("Enter the length of side A: "))
b = float(input("Enter the length of side B: "))
c = float(input("Enter the length of side C: "))

# First, check if the sides can form a valid triangle
if (a + b > c) and (a + c > b) and (b + c > a):
    # Classify the triangle
    if a == b == c:
        print("🔺 The triangle is Equilateral (all sides are equal).")
    elif a == b or b == c or a == c:
        print("🔺 The triangle is Isosceles (two sides are equal).")
    else:
        print("🔺 The triangle is Scalene (no sides are equal).")
else:
    print("❌ The given sides do not form a valid triangle.")
