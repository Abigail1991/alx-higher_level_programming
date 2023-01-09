#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list:
        my_list.reversed()
        for i in range(len(my_list)):
            print("{:d}".format(my_list[i]))
