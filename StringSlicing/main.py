
# Slicing -> Create a substring, extracting elements from the other string.
#       indexing[] or slice()
#       [start:stop:step]

name = "Luis Reis"

first_name = name[0:4]
last_name = name[5:9]
funky_name = name[0:9:2]        #[::2]
reversed_name = name[::-1]

print(first_name)
print(last_name)
print(funky_name)
print(reversed_name)

#Using the slice function.
website = "http://google.com"
website2 = "http://wikipedia.com"

slice_value = slice(7, -4)            #Preparation of the method slice.
slice_value2 = slice(7, -4)

name_website = website[slice_value]
name_website2 = website2[slice_value2]

print(name_website)
print(name_website2)

