
# Functions -> A block of code which is executed when is called.

def hello():
    print("Hello World")
    print("Have a nice day!")

hello()     #Calling the function.
hello()
hello()

def hello2(name: str):
    print("Hello " + name)

hello2("Luis")
hello2("Test")

name_person = "Pedro Castro"

hello2(name_person)

def hello3(first_name: str, last_name: str, age: int):
    print("Hello " + first_name + " " + last_name)
    print("You age is: " + str(age))

hello3("Luis", "Reis", 25)