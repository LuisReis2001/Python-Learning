
# Tuple -> Collection which is ordered and unchangeable, used to group together related data.

student = ("Luis", 25, "Male")

#Methods for tuples.
print(student.count("Luis"))        #Count the amount that shows up.

print(student.index("Male"))        #Index of the value searched.

for i in student:
    print(i)                        #Print the information of the tuple.

if "Luis" in student:
    print("Luis is here.")

