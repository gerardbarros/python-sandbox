# Python has functions for creating, reading, updating, and deleting files.

# Open a file
myFile = open("myfile.txt", "w")

# Get some info
print("Name: ", myFile.name)
print("Is Closed: ", myFile.closed) # asks if clsoed within the script
print("Opening Mode: ", myFile.mode)

# Write to file
myFile.write("I am recieving the offer letter for this software developer job")
myFile.write(" the offer will be sent within this week")
myFile.close()

# Append to file
myFile = open("myFile.txt", "a")
myFile.write(" I will accept the offer and opportunity")
myFile.close()

# Read from file
myFile = open("myFile.txt", "r+")
text = myFile.read(100)
print(text)