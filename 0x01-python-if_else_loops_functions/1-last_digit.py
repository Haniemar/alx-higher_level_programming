#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
l = str(number)
la = l[-1]
la = int(la)
string = "Last digit of"
if la > 5:
    print("{0} {1} is {2} and is greater than 5".format(string, l, la))
elif la == 0:
    print("{0} {1} is {2} and is 0".format(string, l, la))
elif la < 0 and la != 0:
    print("{0} {1} is {2} and is less than 6 and not 0".format(string, l, la))
