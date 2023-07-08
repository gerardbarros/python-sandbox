# A function is a block of code which only runs when it is called. In Python, we do not use parentheses and curly brackets, we use indentation with tabs or spaces

# Create function
def sayHello(name = "Sam"):
    print(f"Hello, {name}")

# Return values
def getSum(num1, num2):
    total = num1 + num2
    return total

num = getSum(3, 4)
print(num)

# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions

getSum = lambda num1, num2 : num1 + num2

print(getSum(10, 5))


# Nested functions
# have access to outer variables, helpful in recursive probs
# can also keep code concise when doing graphs
def outer(a, b):
    c = "c"

    def inner(): #wil have access to all vars in outer
        return a + b + c
    return inner()

print(outer("q", "x"))

# can modify obj but not reasssing vals unless use nonlocal keyword
def double(arr, val): #double every val in arr and val that's not an arr
    def helper():
        # modifying arr works
        for i, n in enumerate(arr):
            arr[i] *= 2

        # will only modify val in helper scope, so val *= 2
        # to update val outside the helper scope, have to declare it as nonlocal val
        nonlocal val
        val *= 2
    helper()
    print(arr, val)

numbers = [1, 2]
val = 3
double(numbers, val)