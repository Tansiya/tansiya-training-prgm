"""write a program to print the list after removing the 0th, 2nd, 4th,6th numbers in [12,24,35,70,88,120,155]"""

#assigned a list

li = [12,24,35,70,88,120,155]

#removing the nposition number 0,2nd,4th,6th

li = [x for (i,x) in enumerate(li) if i%2!=0]

#print list

print (li)
