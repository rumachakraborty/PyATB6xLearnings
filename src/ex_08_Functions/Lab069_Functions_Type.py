#User defined
#1. they cannot return->non return
#2.they will return
#3. they have parameters
#4. they dont have parameters/arguments

#Built in  functions
import  math
result=max(3,7)
print(result)

#1.  they cannot return->non return
#No return type and no parameter/argument

def greet():
    print("Hello")
greet()

#2. no return type and with argument/parameter
def greet_by_name(name):
    print("Hello",name)
greet_by_name("SunnyBoy")

#3. no return type and with default argument/parameter
def say_hello_default_argument(name="ruma"):
    print("Hello",name.upper())
say_hello_default_argument("Chakraborty")
say_hello_default_argument()

#5 multiple args
def multiple_args(name1="A",name2="B"):
    print("MUL->",name1,name2)
multiple_args()
multiple_args(name1="Lucky", name2="sharma")
multiple_args(name1="sunny")
multiple_args(name1="Sunny", name2="bunny")
multiple_args(name2="Hiya")

#4. argument +return type
def sum_of_two_number(a,b):
    return a+b
result=sum_of_two_number(2,8)
print(result)
def sum_of_two_number_with_default(num1=100,num2=200):
    print("Sum of two numbers:")
    return num1+num2
result=sum_of_two_number_with_default(num1=100,num2=200)
print(result)
result1=sum_of_two_number_with_default()
print(result1)