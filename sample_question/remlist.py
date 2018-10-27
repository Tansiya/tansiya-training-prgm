"""list comprehension, write a program to print the list after removing the value 24 in [12,24,35,24,88,120,155]"""

#create a list

li = [12,24,35,24,88,120,155]

#removing 24 divisible numbers

li = [x for x in li if x!=24]

#print list

print (li)

