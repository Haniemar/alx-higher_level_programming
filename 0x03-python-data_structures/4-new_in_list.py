#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 :
        new_list = mylist.copy()
        return(new_list)
    elif idx > len(my_list) - 1:
        new_list = mylist.copy()
        return(new_list)
    new_list = my_list.insert(idx, element)
    return(new_list)
