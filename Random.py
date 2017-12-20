import random
import time

def Random1():
    input = ("Press any key to cast the die:")
    r = list(range(1,7))
    print("Result:",random.choice(r))


while True:
    time.sleep(1)
    Random1()