# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Read more about dictionaries at https://docs.python.org/3/tutorial/datastructures.html#dictionaries

# It's like an object in JS

# Create dictionary
person = {
    "first_name": "John",
    "last_name": "Doe",
    "age": 30
}

# Using constructor
# person2 = dict(first_name = "Yor", last_name = "Forger")

# Get value
print(person["first_name"])

print(person.get("last_name"))

# Add key value
person["phone"] = "555-555-5555"

# Get dict keys
print(person.keys())

# Get dict items
print(person.items())

# Copy dict
person2 = person.copy()
person2["city"] = "Austin"

# Remove item
del(person["age"])
person.pop("phone")

# Clear
person.clear()

# Get length
print(len(person2))

# List of dict
people = [
    {"name": "Martha", "age": 30},
    {"name": "Kevin", "age": 25}
]

print(people[1]["name"])