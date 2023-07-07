# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods
name = "Gerard"
age = 29

# Concatenate
# print("Hello, my name is " + name + " I am " + str(age))

# String Formatting
# Positional arguments
# print("My name is {name}, I am {age}".format(name = name, age = age))

#F-strings (python 3.6+)
print(f"Hello, I am {name}, I am {age} years old")

# String Methods
str = "hello world"

# Capitalize str
print(str.capitalize())