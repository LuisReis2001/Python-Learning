
# Sets -> Collection which is unordered, unindexed. No duplicated values.

utensils = {"Fork", "Spoon", "Knife"}
dishes = {"Bowl", "Plate", "Cup"}

for i in utensils:
    print(i)

#Methods of sets.
utensils.add("Napkin")          #Add to the set.

utensils.remove("Fork")         #Remove the item of the set.

for i in utensils:
    print(i)

utensils.clear()                #Clear the set.

utensils.update(dishes)         #Add the dishes to the utensils set.

dinner = utensils.union(dishes) #Union of the sets to a new value.

print(utensils.difference(dishes)) #Comparation of two sets and get the difference.

print(utensils.intersection(dishes))    #Comparation of what they have in common.

