import math
import random as rand

# ^^^ everytime we want to "include" a package in Python, we must
# use the "import" statement

# sometimes we need other functions from various packages
# for example, the 'maths' package
# https://docs.python.org/3/library/math.html

# why try to make something new when some nerd made this for us already?
# jk, we are the nerds in this case

res1 = math.ceil(4.93)
print(res1)

res2 = math.floor(4.93)
print(res2)

res3 = math.factorial(5)
print(res3)

# this will be useful for us when we begin doing stats & machine learning

# package alias
some_number = rand.randint(0, 100)
print("think of a number...")
print("is it THIS NUM?", some_number)