"""write a program to print the list after removing delete numbers which are divisible by 5 and 7 in [12,24,35,70,88,120,155]"""

#assigned a list

li = [12,24,35,70,88,120,155]

#removing divisible by 5 and 7

li = [x for x in li if x%5!=0 and x%7!=0]

#print list

print (li)


