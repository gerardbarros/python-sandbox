# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

# Create tuple
fruits = ("Apples", "Blueberry", "Oranges", "Grapes")
fruits2 = tuple(("Apples", "Blueberry", "Oranges", "Grapes"))

# For single value tuples, add trailing comma or else it will be treated as a string
fruits3 = ("Mangoes", )

print(fruits[1])

# Tuples cant change value
# fruits[0] = "Pears" #will return an error

# Delete typle
del fruits3

# Find length
print(len(fruits))




# A Set is a collection which is unordered and unindexed. No duplicate members.

# Create set
fruits_set = {"Apple", "Oranges", "Mangoes"}

# Check if in set
print("Apples" in fruits_set)

# Add to set
fruits_set.add("Grapes")

# Remove from set
fruits_set.remove("Grapes")

# If adding duplicate value
fruits_set.add("Apple")

# Clear set
# fruits_set.clear()

# Delete set
# del fruits_set


print(fruits_set)