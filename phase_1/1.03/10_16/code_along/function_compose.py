import math
import statistics

# just like in maths, we can compose functions!
# composition just means combination

# for example! let's say I want to print out the ceiling of 4.93
res1 = math.ceil(4.93)
print(res1)

# the above is unnecessary, I can simply do
print(math.ceil(4.93))

# I am putting a function inside of another function
# Python will first "interpret" the inner function
# and the finally interpret the outer!

# of course, you can many functions inside one another, but that is
#  bad practice imagine trying to read this

print(math.ceil(math.floor(math.log10(math.sqrt(20)))))

# try it yourself
# TODO: calculate and print the median of the list below in one line of code
# take a look at these docs
# https://docs.python.org/3/library/statistics.html
stocks = [7.34, 8.12, 7.20, 9.10, 5.20]
...