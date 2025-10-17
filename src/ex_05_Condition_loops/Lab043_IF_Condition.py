# Write a program to take user age
# and let him know he can go to club
# Logic building activity
# step1
# i/p->age,int
# o/o->string(result)->can go to club
# step2->rough logic
"""
age>21->print can go
age<21->print cannot go

"""
#step3
age=int(input("Enter age\n").strip())
if age>=21:
    print("yes","can go to club")
else:
    print("no","Not you can not go to club")
#Step4. Check for the edge cases
#we should consider edge case such as:
#Negative ages or extremly high values->program will break
#Non-numeric input->ABC-> not allowed
#age is valid >130
#step 5 :
try:
    age_input = input("Enter your age: ").strip()
    if not age_input:
        print("Input cannot be empty.")
    else:
        age = int(age_input)
        if age < 0:
            print("Age cannot be negative.")
        elif age > 130:
            print("Please enter a realistic age (below 130).")
        elif age >= 21:
            print("Yes, you can go to the club.")
        else:
            print("No, you cannot go to the club.")
except ValueError:
    print("Invalid input. Please enter a valid number.")




