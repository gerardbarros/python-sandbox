# Hash Sets - search in constant time and insert in constant time
# no duplicates allowed unlike lists

mySet = set()
mySet.add(1)
mySet.add(2)
print(f"First set: {mySet}")
print(len(mySet))

# check for vals in hash set
print(1 in mySet)
print(2 in mySet)
print(3 in mySet)

# can remove vals in constant time 
mySet.remove(2)
print(2 in mySet)

# hash set wit bunch of vals, pass a list
print(set([2, 4, 6]))


# can also do set comprehension manually init with loop inside has set
# go through every val in range of i and taking val and adding to hash set
mySet1 = {i for i in range(6)}
print(mySet1)


# Hash Maps / Dictionary
myMap = {}
# insert
# cant have duplicates
myMap["anya"] = 88
myMap["yor"] = 77
print(myMap)
print(len(myMap))

# can modify value mapped to a key
myMap["anya"] = 80
print(myMap["anya"])

# can also search if key is in hasmmap in constant time and remove key which also removes value

print("anya" in myMap)
myMap.pop("anya")
print("anya" in myMap)


# To init hash map, add pairs in {} and seperated by comma (manual insert)
# myMap1 = {"loid": 50, "franky": 60}
# print(myMap1)

# Dict comprehension, HM are pretty much dictionaries
# Usefull in graph problems and adjacency lists
# To loop i in range of 3, we get 2 vals
myMap2 = { key: 2* key for key in range(4)}
print(myMap2)


# Loop through a map, by default go through every key and print key and its value
myMap1 = {"loid": 50, "franky": 60}
for key in myMap1:
    print(key, myMap1[key])
# can also directly iterate through list of vals of HM if we dont need key
for val in myMap1.values():
    print(val)
# unpacking can go through items of HM which gives key and val
for key, val in myMap1.items():
    print(key, val)