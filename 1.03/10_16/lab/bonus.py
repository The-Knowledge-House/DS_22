import time


# implement the logic found in `bad_code.py`
def log_event(event, path, epoch=time.time()):
   ...


# if your function works as intended, these 3
# function calls should update the "logfile.txt" file
path = "1.03/10_16/lab/logfile.txt"
log_event("pipeline started", path)
log_event("pipeline skipped file", path)
log_event("pipeline ended", path)
