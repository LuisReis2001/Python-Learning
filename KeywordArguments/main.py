
# Keyword Arguments -> Arguments preceded by an identifier when pass them to a function
# The order of the arguments doesn't matter, unlike positional arguments

def hello(first, middle, last):
    print("Hello " + first + " " + middle + " " + last)

hello(first = "Luis", middle = "dos", last = "Reis")