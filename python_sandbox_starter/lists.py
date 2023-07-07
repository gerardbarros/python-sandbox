# A List is a collection which is ordered and changeable. Allows duplicate members.

# Create list
numbers = [1, 2, 3, 4, 5]
fruits = ["Apples", "Oranges", "Grapes", "Mangoes"]

#Use constructor
# numbers2 = list((2, 4, 6, 8))

# Get a value
print(fruits[1])

# Get length
print(len(fruits))

# Add / append to list
fruits.append("Peaches")

# Remove from list
fruits.remove("Grapes")

# insert into position
fruits.insert(2, "Strawberries")

# Change values
fruits[0] = "Blueberry"

# Remove with pop (in position)
fruits.pop(2)

# Reverse
fruits.reverse()

# Sort by alpha order
fruits.sort()

# Reverse sort
fruits.sort(reverse=True)



print(fruits)