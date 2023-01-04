#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit_str = str(number)
last_digit = last_digit_str[-1]
last_digit = int(last_digit)
string = "Last digit of"
if last_digit > 5:
    print("{0} {1} is {2} and is greater than 5".format(string, number, last_digit))
elif last_digit == 0:
    print("{0} {1} is {2} and is zero".format(string, number, last_digit))
elif last_digit < 0 and last_digit != 0:
    print("{0} {1} is {2} and is less than 6 and not 0".format(string, number, last_digit))

