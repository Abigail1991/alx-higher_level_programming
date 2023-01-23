#!/usr/bin/python3
def safe_print_division(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
        return result
