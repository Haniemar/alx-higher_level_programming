#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if ord(char) in range(97, 123):
            c = ord(char) - 32
            print("{}".format(chr(c)), end="")
        else:
            print("{}".format(char), end="")
