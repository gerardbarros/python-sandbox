# A List is a collection which is ordered and changeable. Allows duplicate members.

# Create list
numbers = [1, 2, 3, 4, 5]
fruits = ["Apples", "Oranges", "Grapes", "Mangoes"]

#Use constructor
# numbers2 = list((2, 4, 6, 8))

# Get a value
# print(fruits[1])

# # Get length
# print(len(fruits))

# # Add / append to list
# fruits.append("Peaches")

# # Remove from list
# fruits.remove("Grapes")

# # insert into position
# fruits.insert(2, "Strawberries")

# # Change values
# fruits[0] = "Blueberry"

# # Remove with pop (in position)
# fruits.pop(2)

# # Reverse
# fruits.reverse()

# # Sort by alpha order
# fruits.sort()

# # Reverse sort
# fruits.sort(reverse=True)


# Can use custom sort (like length of string)
fruits.sort(key = lambda val: len(val))
print(fruits)

# List comprehension
# Go through every value in range 5 and call it i and add val to array 
arr = [i for i in range(6)]
print(arr)

# 2D List 
# arr = [[0] * 4] gives an arr of size 4 with all 0s; if we want to add that arr to an outer arr 4x use 2D list:
arr2D = [[0] * 4 for i in range(4)]
print(arr2D)