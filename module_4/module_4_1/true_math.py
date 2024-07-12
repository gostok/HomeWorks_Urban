from math import inf

def divide(first, second):
    
    try:
        print(first / second)
    except ZeroDivisionError:
        print(inf)