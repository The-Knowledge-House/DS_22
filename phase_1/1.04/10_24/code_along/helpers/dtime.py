import time
from datetime import datetime


def get_time():
    epoch = time.time()
    print(datetime.utcfromtimestamp(epoch).strftime('%Y-%m-%d %H:%M:%S'))


if __name__ == "__main__":
    print("you've now ran the dtime module")
    get_time()
