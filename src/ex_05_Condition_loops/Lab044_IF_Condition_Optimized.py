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
if age<=0 or age>130:
    print("Enter a  valid age")
else:
    if age>=21:
        print("Yes Yes , you can go to club")
    else:
        print("you cannot go to club")

