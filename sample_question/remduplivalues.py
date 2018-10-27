"""Given a list [12,24,35,24,88,120,155,88,120,155], write a program to print this list after removing all duplicate values with original order reserved"""

#create a function

def removeDuplicate( li ):
    newli=[]
    seen = set()

#acces the values for loop

    for item in li:

#using if condition

        if item not in seen:
            seen.add( item )
            newli.append(item)

    return newli

#assigned a list

li=[12,24,35,24,88,120,155,88,120,155]

print (removeDuplicate(li))


