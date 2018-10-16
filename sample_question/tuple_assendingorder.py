"""Find the (name, age, height) tuplesby assending order where the name is string, age and height are numbers.the tuples are input by console"""
from  operator import itemgetter, attrgetter

#assign a list
l = []

#using while loop

while True:
	s = input()
#using if loop
	if not s:
		break;
#list append the tuple
	l.append(tuple(s.split(","))) 

#print the sorted tupleand asendingorder
print(sorted(l, key = itemgetter (0, 1, 2)))
