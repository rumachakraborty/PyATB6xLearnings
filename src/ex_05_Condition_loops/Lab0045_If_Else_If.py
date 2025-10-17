#write a program for even and odd number
num=int(input("Enter number\n").strip())
num1=float(input("Enter number\n").strip())
if num>=0:
    if num%2 == 0:
        print("Even")
    else:
        print("odd")
else:
    print("Negative number")

#     Optimize code

if num1 >=0:
    print("Even" if num1%2==0 else "odd")
else:
    print("negative number")
