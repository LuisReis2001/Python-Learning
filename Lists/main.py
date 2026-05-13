
# Lists -> Store multiple items in a single variable.

food = ["pizza", "Hamburger", "Hotdog", "Pasta"]

print(food)     #Print the entire list.

print(food[0])  #Print the first element of the list.

for i in food:
    print(i)

food[0] = "sushi"

print(food[0])

food.append("ice-cream")        #Add to the list.

print(food[4])                  #Print ice-cream.

food.remove("Hamburger")        #Remove the value indicated in the list.

food.pop()                      #Remove the last item.

food.insert(0, "Cake")      #Insert in the position 0 the value Cake.

print(food[0])

food.sort()                     #Sort alphabetic the list.

food.clear()                    #Clear of the list.