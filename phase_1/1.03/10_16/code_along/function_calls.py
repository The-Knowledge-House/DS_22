# REMEMBER: we run code via `python function_calls.py` in the terminal

# we "call" a function in Python by writing out its name
# functions usually take in an argument, and **return** a result

num = 32
strng = '32'
word = 'regression'
floating = 32.24

# this function takes in a string, and returns an int
new_num = int(strng)
print(new_num)

# this function takes in a string, and returns a float
new_float = float(strng)
print(new_float)

# this function takes in an int, and returns a string
new_str = str(num)
print(new_str)

# this function takes in a string, and returns its length
size = len(word)
print("size is", size)

# more specifically, these functions convert one type to another
# AKA TYPE_CAST!
# What does the "type()" function appear to return?
print("previous type", type(strng))
print("new type", type(new_num))

# What happens if we try to give a non-number string to int
# comment the line of code below out to find out!
# test = int(word)

# sometimes however, we do not always return a value!
x = print("hello world")
print(x)

# sure this PRINTS OUT 'hello world', but does it return anything???

# try it yourself
# TODO: convert the 'num' int variable to a string, and get its size
# using functions
...

# fun fact:

# functions that only take in values and return values
# (without modifying objects) are called "pure functions"
# some programmers argue that all functions should be
# "pure functions"!
# or at the very least, they use programming languages that
# only have pure functions
