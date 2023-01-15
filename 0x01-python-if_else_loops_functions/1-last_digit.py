#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if (number < 0):
    nr = ((-number) % 10) * -1
else:
    nr = number % 10
print("Last digit of {:d} is {:d} and is ".format(number, nr), end='')
if (nr > 5):
     print("greater than 5")
elif nr == 0:
    print(" 0")
else:
     print("Less than 6 and not 0")
