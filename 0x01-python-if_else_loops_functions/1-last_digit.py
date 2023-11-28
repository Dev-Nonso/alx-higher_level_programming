#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastdigit = abs(number) % 10
if number < 0:
    lastdigit = -(lastdigit)
n_str = "Lastdigit of {} is {}".format(number, lastdigit)
if lastdigit > 5:
    print(f"{n_str} and is greater than 5")
elif lastdigit == 0:
    print(f"{n_str} and is 0")
else:
    print(f"{n_str} and is less than 6 and not 0")
