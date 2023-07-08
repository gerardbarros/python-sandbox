# Tupes like arr but immutable
tup = (1, 2, 3)
print(tup)
print(tup[0])
print(tup[1])

# Can't modify
# Usually used as keys in hash map/set
myMap = { (1, 2): 3 } # this serves as our hashable key
print(myMap[(1, 2)])

# Can do samething for HS and use the tuple to search HS
mySet = set()
mySet.add((1, 2))
print((1, 2) in mySet)

# Lists cant be keys and not hashable
# myMap[[3, 4]] = 5; this won't work