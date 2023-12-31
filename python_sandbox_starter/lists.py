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


# Can be used as a stack
arr.append(4)
arr.append(5)
print(arr)

arr.pop()
print(arr)

arr.insert(1, 7)
print(arr)

arr[0] = 0
arr[3] = 0
print(arr)

# Initialize arr of size n with default value of 1
n = 5
arr = [1] * n
print(arr)
print(len(arr))

# Careful: -1 is not out of bounds, it's the last value
arr = [1, 2, 3]
print(arr[-1])

# Indexing -2 is the second to last value, etc.
print(arr[-2])

# Sublists (aka slicing)
arr = [1, 2, 3, 4]
print(arr[1:3])

# Similar to for-loop ranges, last index is non-inclusive
print(arr[0:4])

# But no out of bounds error
print(arr[0:10])

# Unpacking
a, b, c = [1, 2, 3]
print(a, b, c)

# Be careful though
# a, b = [1, 2, 3]

# Loop through arrays
nums = [1, 2, 3]

# Using index
for i in range(len(nums)):
    print(nums[i])

# Without index
for n in nums:
    print(n)

# With index and value
for i, n in enumerate(nums):
    print(i, n)

# Loop through multiple arrays simultaneously with unpacking
nums1 = [1, 3, 5]
nums2 = [2, 4, 6]
for n1, n2 in zip(nums1, nums2):
    print(n1, n2)

# Reverse
nums = [1, 2, 3]
nums.reverse()
print(nums)

# Sorting
arr = [5, 4, 7, 3, 8]
arr.sort()
print(arr)

arr.sort(reverse=True)
print(arr)

arr = ["bob", "alice", "jane", "doe"]
arr.sort()
print(arr)


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