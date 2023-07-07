# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary

import json

# Sample JSON
userJSON = '{"first_name": "Loid", "last_name": "Forger", "age": 30}'

# Parse to dict
user = json.loads(userJSON)

# print(user)
# print(user["first_name"])

# Take dictionary convert to JSON

car = {"make": "Nissan", "model": "skyline", "year": 1992}
carJSON = json.dumps(car)

print(carJSON)