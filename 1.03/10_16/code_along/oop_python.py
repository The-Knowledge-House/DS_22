# you've been creating "objects" all this time!
word = "hello world!"

# a string is an object!

# it contains attributes
print(word.__annotations__)

# it also contains methods
print(word.capitalize())

# we might not know what operations are going on behind the scenes...
# but it won't matter
# encapsulation and abstraction allows us to do more complex operations
# without worrying about the internals of a string

# as it turns out, everything is an object in Python:
 # https://jakevdp.github.io/WhirlwindTourOfPython/03-semantics-variables.html#Everything-Is-an-Object