#!/usr/bin/python3
def element_at(my_list, idx):
    for index in range(len(my_list)):
        if index < 0:
            return None
        elif index > len(my_list):
            return None
        else:
            return mylist[index]
