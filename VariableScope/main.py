
# Scope -> The region that a variable is recognized.
# LEGB order -> Local variables, enclosing variable, global variable and built-in variable.

name = "Test"               #Global scope for all the file.

def display_name():
    name_local = "Code"           #Local scoped in the function.
    print(name_local)

display_name()
print(name)