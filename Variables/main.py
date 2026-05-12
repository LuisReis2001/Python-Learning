
#Variable is a container for a value.
##Variable of string str.
name = "Luis"
print(name)                 #Print Luis
print("Hello " + name)      #Print Hello Luis
print(type(name))           #Print the type of the variable name

first_name = "Luis"
last_name = "Reis"
full_name = first_name + " " + last_name
print(full_name)            #Print Luis Reis

##Variable of integer int.
age = 25
age = age + 1
age += 1
print(age)                  #Print 27
print(type(age))            #Print int
#print("Your age is: " + age) #It gives error
print("Your age is: " + str(age)) #Print Your age is: 27

##Variable of float.

height = 150.5
print(height)               #Print 150.5
print(type(height))         #Print float
print("Your height is: " + str(height) + "cm") #Print Your height is: 150.5cm

##Variable of Boolean.

human = False
print(human)                #Print False
print(type(human))          #Print Bool
print("Are you a human: " + str(human))     #Print Are you a human: False
