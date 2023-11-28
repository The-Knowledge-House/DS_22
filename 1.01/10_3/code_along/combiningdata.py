"""
Combining data types
"""
num1 = 3
num2 = num1 + 2

pi = 3.14

word = "hello"

on = True
off = False
foobar = True

# which data type is this?
y = input("type something here.")

# does this work? why or why not?
print(word + y)

# how about this?
print(num1 + word)

# what can we do to make this work?
print(num1 + word)

# data-type conversions

# what type do we see here?
print(type(num1 + num1))

# how about here?
print(type(num1 + pi))

# surprises
print(num1 + pi)

# and fixes

# floating point error explained:
#   https://realpython.com/lessons/floating-point-representation-error/

# this isn't a problem for us, unless you need those milliseconds: 
#   http://www.cs.unc.edu/~smp/COMP205/LECTURES/ERROR/lec23/node4.html