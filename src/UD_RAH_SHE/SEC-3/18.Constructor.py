#classes are nothing but
class calculator:
    # class variable are constant
    num=10
    # constructor
    def __init__(self,a,b):
        print("I AM FROM internal method which from constructor")
        self.num1=a
        self.num2=b

    def summation(self):
        return self.num1 + self.num2

    print(summation(1, 2))



    def getData(self):
        print("i am executing a method in class")
obj=calculator(2,3)
obj.getData()
print(obj.num)


obj1=calculator(2,4)
obj1.getData()
print(obj1.num)

# summ


