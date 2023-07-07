# A variable is a container for a value, which can be of various types

'''
This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""

x = 1 #int as default
y = 2.5 #float by default
name = "John" #str
is_cool = True # bool, has to be cap T or F for False

# Multiple assignements
x, y, name, is_cool = (1, 2.5, "James", False)

# Quick maffs
a = x + y

# Casting - changes types 
x = str(x)
y = int(y)
z = float(y) 

# Check type of var
print(type(x))
print(type(y), y)
print(type(z), z)



# print("Hello")
# print(x, y, name, is_cool, a)