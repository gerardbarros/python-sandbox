# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

people = ["Anya", "Loid", "Yor", "Bond"]

# # simple for loop
# for person in people:
#     print(f"Curent Person: {person}")

# Break
# for person in people:
#     if person == "Yor" : 
#         break
#     print(f"Current person: {person}")

# Continue
# for person in people:
#     if person == "Yor" : 
#         continue
#     print(f"Current person: {person}")

# Range
# for i in range(len(people)):
#     print(people[i])

# for i in range(0, 11):
#     print(f"Number: {i}")

# While loops execute a set of statements as long as a condition is true.
# count = 0
# while count <= 10:
#     print(f"Count: {count}")
#     count += 1

# for i in range(10, 1, -2):
#     print(f"Current number: {i}")

# Loop through arr
nums = [1, 2, 3]
print(f"Number: {nums}")

# Using index
for i in range(len(nums)):
    print(f"Current num: {nums[i]}")


# Without index
for n in nums:
    print(f"Number: {nums}")


# With index and val (enumerate)
for i, n in enumerate(nums):
    print(f"Index: {i}, Element: {n}")