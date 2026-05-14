
# Index Operator [] -> Gives access to a element of (str, list, tuples)

name = "Luis Reis!"

if (name[0].islower()):
    name = name.capitalize()

print(name)

first_name = name[0:4].upper()      #Getting the first name.
last_name = name[5:].upper()        #Getting the last name.

print(first_name)
print(last_name)

last_character = name[-1]           #Getting the last element.

print(last_character)