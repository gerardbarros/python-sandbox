# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

# Create class
class User:
    # Constructor
    def __init__(self, name, email, age):
        # member variables
        self.name = name
        self.email = email
        self.age = age
    def greeting(self):
        return f"My name is {self.name}, I am {self.age}"
    def has_birthday(self):
        self.age += 1


# Extend class
class Customer(User):
    # Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0
    def set_balance(self, balance):
        self.balance = balance
    def greeting(self):
        return f"My name is {self.name}, I am {self.age}. My current balance is {self.balance}"

# Init user object
brad = User("Brad Traversy", "brad@gmail.com", 37)

# Init customer object
janet = Customer("Janet Jackson", "janet@gmail.com", 25)

janet.set_balance(500)
print(janet.greeting())

brad.has_birthday()
print(brad.greeting())


class MyClass:
    # Constructor
    def __init__(self, nums):
        # Create member variables
        self.nums = nums
        self.size = len(nums)
    
    # self key word required as param
    def getLength(self):
        return self.size

    def getDoubleLength(self):
        return 2 * self.getLength()

myObj = MyClass([1, 2, 3])
print(myObj.getLength())
print(myObj.getDoubleLength())
