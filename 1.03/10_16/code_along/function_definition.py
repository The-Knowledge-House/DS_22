# simple function definition
# no parameters
def adder23():
    return 2 + 3


# functions with parameters
def adderVar(x):
    return x + 5


# functions with parameters
def adder(x, y):
    return x + y


# functions with default parameters
def adderblank(x=6, y=5):
    return x + y


# functions with no return
def adderNoRet(x, y):
    x + y


# try it yourself
# TODO: Create a function that takes in two numbers and multiplies them
# together
...

# TODO: and then call this function to calc 2 * 2
...

res0 = adderVar(2)
print("adderVar(2)", res0)

# let's see what happens when we don't call a function with parentheses
# or arguments...
resError = adderVar
print("what will happen here...", resError)

res1 = adder23()
print("adder23()", res1)

res2 = adder(8, 9)
print("adder(8, 9)", res2)

res3 = adderblank()
print("adderblank()", res3)

res4 = adderblank(15, 10)
print("adderblank(15, 10)", res4)

res5 = adderNoRet(15, 10)
print("adderNoRet(15, 10)", res5)

