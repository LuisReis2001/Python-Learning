
# Dictionary -> A changeable, unordered collection of unique key:value pairs.
# Fast because they use hashing to access the value.

capitals = {"USA": "Washington DC", "India": "New Dehli", "China": "Beijing", "Russia": "Moscow"}

print(capitals["Russia"])       #Print the value of the key russia.
print(capitals.get("China"))
print(capitals.get("Germany"))  #Print None since doesn't exist.

print(capitals.keys())          #Print the keys.
print(capitals.values())        #Print the values.

print(capitals.items())         #Print the entire dictionary.

for key, value in capitals.items():
    print(key, value)           #Same as items().

capitals.update({"Germany": "Berlin"})      #Add a new value to the dictionary.

capitals.update({"USA": "Las Vegas"})       #Update the key USA.

capitals.pop("Germany")                 #Remove the key, value from the dictionary.

capitals.clear()                        #Clear the dictionary.

