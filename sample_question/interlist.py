"""write a program to  lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155], write a program to make a list whose elements are intersection of the above given lists"""

#create set1,2

set1=set([1,3,6,78,35,55])

set2=set([12,24,35,24,88,120,155])

#using & intersection operator

set1 &= set2

#assigned list

li=list(set1)

#print list

print (li)

