import time

event = "pipeline started"
path = "1.03/10_16/lab/logfile.txt"

str_build = str(time.time()) + ":" + event + "\n"
with open(path, "a") as file:
    file.write(str_build)

event2 = "pipeline skipped file"
str_build = str(time.time()) + ":" + event2 + "\n"
with open(path, "a") as file:
    file.write(str_build)

event3 = "pipeline ended"
str_build = str(time.time()) + ":" + event3 + "\n"
with open(path, "a") as file:
    file.write(str_build)

# I cry everytime :'(

# can you imagine making a bug in one of those code-blocks?
# since this is a simple copy-paste job, it would cost me 
# a lot to just fix one bug

# this is pretty bad code, can you figure out how to capture this logic
# and turn it into a function in `bonus.py`?